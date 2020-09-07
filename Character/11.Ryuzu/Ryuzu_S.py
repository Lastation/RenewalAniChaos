

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000000);
		SetMemory(0x58E89C, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000000);
		SetMemory(0x58E898, Subtract, 0x00000000);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000000);
		SetMemory(0x58E89C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000000);
		SetMemory(0x58E898, Add, 0x00000000);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(230);
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000000);
		SetMemory(0x58E898, Add, 0x00000000);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000000);
		SetMemory(0x58E89C, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000000);
		SetMemory(0x58E898, Subtract, 0x00000000);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000000);
		SetMemory(0x58E89C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(230);
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(50);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
	},
}