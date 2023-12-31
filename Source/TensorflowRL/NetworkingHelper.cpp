#include "NetworkingHelper.h"

#include "Interfaces/IPv4/IPv4Address.h"
#include "Networking.h"
#include "Sockets.h" // For socket-related functionalities
#include "SocketSubsystem.h" // For ISocketSubsystem
#include "UObject/NameTypes.h"

//CreateSocket(const FName& SocketType, const FString& SocketDescription, bool bForceUDP = false)

void UNetworkingHelper::InitiateClient()
{
	UE_LOG(LogTemp, Warning, TEXT("PRINTING FROM C++"));
	//FIPv4Address IPAddress;
	FString host = FString("127.0.0.1"); // IP ADDRESS
	FString port = FString("8080");

	ESocketProtocolFamily family = ESocketProtocolFamily::IPv4;
	ISocketSubsystem* SocketSubsystem = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM);
	if (SocketSubsystem) {
		FSocket* socket = SocketSubsystem->CreateSocket(FName(TEXT("TCP")), FString("UDP IPV4 Socket"), family);
		//Connect(const FInternetAddr& Addr)

		/**
		 * Sends a buffer on a connected socket.
		 *
		 * @param Data The buffer to send.
		 * @param Count The size of the data to send.
		 * @param BytesSent Will indicate how much was sent.
		 */
		// bool Send(const uint8* Data, int32 Count, int32& BytesSent);
		// RecvFrom(uint8* Data, int32 BufferSize, int32& BytesRead, FInternetAddr& Source, ESocketReceiveFlags::Type Flags = ESocketReceiveFlags::None);
		// Recv(uint8* Data, int32 BufferSize, int32& BytesRead, ESocketReceiveFlags::Type Flags = ESocketReceiveFlags::None);
	}
	else {
		UE_LOG(LogTemp, Error, TEXT("Failed to construct a socket subsystem object"));
	}
		//FIPv4Address::Parse(FString("127.0.0.1"), IPAddress);
	// create socket
	//FSocket* CharacterSocket = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->CreateUniqueSocket(NAME_Stream);
	// connect 

	// send/recv
}
