// Fill out your copyright notice in the Description page of Project Settings.
//https://www.youtube.com/watch?v=zuJ2tjZW770

#include "FileInteract.h"
#include <Runtime\Core\Public\Misc\Paths.h>
#include <Runtime\Core\Public\HAL\PlatformFileManager.h>

FString UFileInteract::LoadFileToString(FString Filename) {
	FString directory = FPaths::ProjectContentDir();
	FString result;
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();

	if (file.CreateDirectory(*directory)) {
		FString myFile = directory + "/" + Filename;
		FFileHelper::LoadFileToString(result, *myFile);
	}
	return result;
}