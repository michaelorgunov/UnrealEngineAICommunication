// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include <D:/Epic Games/UE_5.3/Engine/Source/Runtime/Core/Public/Misc/FileHelper.h>
#include "FileInteract.generated.h"

/**
 * 
 */
UCLASS()
class TENSORFLOWRL_API UFileInteract : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
		UFUNCTION(BlueprintCallable, category="File I/O")
		static FString LoadFileToString(FString Filename);

		UFUNCTION(BlueprintCallable, category = "File I/O")
		static FString LoadStringToFile(FString Filename, FString Message);

		UFUNCTION(BlueprintCallable, category = "File I/O")
		static FString LoadStringArrayToFile(FString Filename, TArray<FString> MessageArray);
};
