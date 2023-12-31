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
UCLASS()
class TENSORFLOWRL_API UNetworkingHelper : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	public:
		UFUNCTION(BlueprintCallable, category = "TCP")
		static bool InitiateClient(FString HostIPAddress, int PortNumber);
		UFUNCTION(BlueprintCallable, category = "TCP")
		static bool SendData(const TArray<uint8>& DataToSend);
		UFUNCTION(BlueprintCallable, category = "TCP")
		static bool ReceiveData(TArray<uint8>& ReceivedData);
		UFUNCTION(BlueprintCallable, category = "TCP")
		static TArray<uint8> StringToByteArray(FString InputString);
		UFUNCTION(BlueprintCallable, category = "TCP")
		static FString ByteArrayToString(TArray<uint8> ByteArray);
	private:
		static FSocket* socket;
};
