// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "NetworkingHelper.generated.h"

/**
 * 
 */
UCLASS()
class TENSORFLOWRL_API UNetworkingHelper : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	UFUNCTION(BlueprintCallable, category = "Networking")
	static void InitiateClient();
	
};
