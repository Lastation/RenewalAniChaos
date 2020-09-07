
Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}
