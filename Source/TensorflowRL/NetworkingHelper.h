#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Networking.h"
#include "Sockets.h"
#include "SocketSubsystem.h"
#include "NetworkingHelper.generated.h"

/**
 * 
 */
UCLASS(BlueprintType)
class TENSORFLOWRL_API UNetworkingHelper : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	public:
		UFUNCTION(BlueprintCallable, category = "TCP")
		bool InitiateClient(FString HostIPAddress, int PortNumber);
		UFUNCTION(BlueprintCallable, category = "TCP")
		bool SendData(const TArray<uint8>& DataToSend);
		UFUNCTION(BlueprintCallable, category = "TCP")
		bool ReceiveData(TArray<uint8>& ReceivedData);
		UFUNCTION(BlueprintCallable, category = "TCP")
		TArray<uint8> StringToByteArray(FString InputString);
		UFUNCTION(BlueprintCallable, category = "TCP")
		FString ByteArrayToString(TArray<uint8> ByteArray);
	private:
		FSocket* socket;
};
