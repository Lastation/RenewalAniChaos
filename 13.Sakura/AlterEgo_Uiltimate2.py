Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("10.AlterEgo_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Fenix", CurrentPlayer, "Anywhere", Move, "10.AlterEgo_Bozo");
		ModifyUnitShields(All, " * Fenix", CurrentPlayer, "Anywhere", 5);
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, " Unit. Polarlicht", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("[Unique]AlterEgo", " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "[Unique]AlterEgo");
		MoveLocation("[Unique]AlterEgo", " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "[Unique]AlterEgo");
		MoveLocation("[Unique]AlterEgo", " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "[Unique]AlterEgo");
		MoveLocation("[Unique]AlterEgo", " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "[Unique]AlterEgo");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		Wait(500);
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Gantrithor", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("120 + 1n Archon", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(2000);
		ModifyUnitHangarCount(8, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(2800);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(AllPlayers, SetTo, 10011, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("40 + 3n Zeratul", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(1600);
		SetDeaths(AllPlayers, SetTo, 10012, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 4, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(130);
		KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 4, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 3, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 4, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}
