import unreal

actor_to_spawn = unreal.load_asset("/Game/Dynamic/BlueprintsSunny/PLAYER_BLUEPRINT.PLAYER_BLUEPRINT")
unreal.EditorLevelLibrary().spawn_actor_from_object(actor_to_spawn, [0, 0, 124])