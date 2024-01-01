#include "NetworkingHelper.h"

#include "Interfaces/IPv4/IPv4Address.h"
#include "Networking.h"
#include "Sockets.h"
#include "SocketSubsystem.h" 
#include "UObject/NameTypes.h"

//CreateSocket(const FName& SocketType, const FString& SocketDescription, bool bForceUDP = false)
//FSocket* UNetworkingHelper::socket = nullptr;

//UNetworkingHelper::UNetworkingHelper()
//{
//	ESocketProtocolFamily family = ESocketProtocolFamily::IPv4;
//	ISocketSubsystem* SocketSubsystem = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM);
//	if (SocketSubsystem) {
//		UE_LOG(LogTemp, Display, TEXT("TCP: SUCCESSFULLY CREATED SOCKET SUBSYSTEM"));
//		// Create socket
//		socket = SocketSubsystem->CreateSocket(FName(TEXT("TCP")), FString("UDP IPV4 Socket"), family);
//	}
//}
//
//UNetworkingHelper::~UNetworkingHelper()
//{
//	if (socket) {
//		socket->Close();
//		ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->DestroySocket(socket);
//		socket = nullptr;
//	}
//}

bool UNetworkingHelper::InitiateClient(FString HostIPAddress, int PortNumber)
{
	//FIPv4Address IPAddress;
	FString host = HostIPAddress; //EX: FString("127.0.0.1");
	int port = PortNumber; //EX: FString("8080");

	// Get platform for different socket functions
	ESocketProtocolFamily family = ESocketProtocolFamily::IPv4;
	ISocketSubsystem* SocketSubsystem = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM);
	if (SocketSubsystem) {
		UE_LOG(LogTemp, Display, TEXT("TCP: SUCCESSFULLY CREATED SOCKET SUBSYSTEM"));
		// Create socket
		socket = SocketSubsystem->CreateSocket(FName(TEXT("TCP")), FString("UDP IPV4 Socket"), family);
		if (socket) { 
			UE_LOG(LogTemp, Display, TEXT("TCP: SUCCESSFULLY CREATED SOCKET"));
			// Create IP Address
			FIPv4Address ip;
			FIPv4Address::Parse(HostIPAddress, ip);

			TSharedPtr<FInternetAddr> address = SocketSubsystem->CreateInternetAddr();
			address->SetIp(ip.Value);
			address->SetPort(port);
			
			// Connect to server
			bool connected = socket->Connect(*address);
			if (connected) {
				UE_LOG(LogTemp, Display, TEXT("TCP: SUCCESSFULLY CONNECTED"));
				return true;
			}
			else {
				UE_LOG(LogTemp, Error, TEXT("Failed to establish connection"));
				return false;
			}
		}
		else {
			UE_LOG(LogTemp, Error, TEXT("Failed to create socket"));
			return false;
		}
	}
	else {
		UE_LOG(LogTemp, Error, TEXT("Failed to construct a socket subsystem object"));
		return false;
	}
}

bool UNetworkingHelper::SendData(const TArray<uint8>& DataToSend)
{
	if (socket) {
		int32 port = socket->GetPortNo();
		UE_LOG(LogTemp, Warning, TEXT("SEND TO PORT: %d"), port);

		int32 BytesSent = 0;
		bool success = socket->Send(DataToSend.GetData(), DataToSend.Num(), BytesSent);
		if (success) {
			UE_LOG(LogTemp, Warning, TEXT("Sent Data"));
			return true;
		}
		else {
			UE_LOG(LogTemp, Error, TEXT("Failed to send data"));
			return false;
		}
	}
	else {
		UE_LOG(LogTemp, Error, TEXT("Invalid socket"));
		return false;
	}
}

bool UNetworkingHelper::ReceiveData(TArray<uint8>& ReceivedData)
{
	//if (socket) {
	//	uint32 PendingDataSize = 0;
	//	while (socket->HasPendingData(PendingDataSize) && PendingDataSize > 0)
	//	{
	//		TArray<uint8, TInlineAllocator<1024>> ReceivedData;
	//		ReceivedData.SetNumZeroed(PendingDataSize + 1);

	//		int32 BytesRead = 0;
	//		if (socket->Recv(ReceivedData.GetData(), ReceivedData.Num(), BytesRead) && BytesRead > 0)
	//		{
	//			ReceivedData.Last() = 0; // Ensure null terminator
	//		}
	//	}
	//	UE_LOG(LogTemp, Warning, TEXT("Received Data"));

	//	return true;
	if (socket) {
		//UE_LOG(LogTemp, Display, TEXT("TCP RECEIVE: Valid Socket == True"));
		int32 port = socket->GetPortNo();
		UE_LOG(LogTemp, Warning, TEXT("RECIEVE FROM PORT: %d"), port);
		uint32 size;
		if (socket->HasPendingData(size)) {
			//UE_LOG(LogTemp, Display, TEXT("TCP RECEIVE: Has Pending Data == True"));

			int32 bytesRead = 0;
			int32 bufferSize = 1024;
			ReceivedData.SetNumUninitialized(bufferSize);
			bool success = socket->Recv(ReceivedData.GetData(), ReceivedData.Num(), bytesRead);

			if (success && bytesRead > 0) {
				ReceivedData.SetNum(bytesRead);
				return true;
			}
			else {
				UE_LOG(LogTemp, Error, TEXT("Failed to receive data from server. success: %"), success);
				return false;
			}
		}
		else {
			UE_LOG(LogTemp, Error, TEXT("No data available to receive from server"));
			return false;
		}
	}
	else {
		UE_LOG(LogTemp, Error, TEXT("Invalid socket"));
		return false;
	}
}

TArray<uint8> UNetworkingHelper::StringToByteArray(FString InputString)
{
	TArray<uint8> byteArray;
	const TCHAR* stringPtr = *InputString;
	if (InputString.Len() > 0) {
		while (*stringPtr)
		{
			// Retrieve the ASCII value of each character in the string
			uint8 charByte = static_cast<uint8>(*stringPtr);
			byteArray.Add(charByte);

			++stringPtr;
		}
	}
	return byteArray;
}

FString UNetworkingHelper::ByteArrayToString(TArray<uint8> ByteArray)
{
	FString resultString;
	if (ByteArray.Num() > 0) {
		for (uint8 byteValue : ByteArray)
		{
			// Convert each byte value back to its ASCII character equivalent
			TCHAR charValue = static_cast<TCHAR>(byteValue);
			resultString.AppendChar(charValue);
		}
	}
	else {
		return " ";
	}

	return resultString;
}
