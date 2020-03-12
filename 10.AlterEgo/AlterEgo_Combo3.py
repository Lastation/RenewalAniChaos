Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("10.AlterEgo_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Fenix", CurrentPlayer, "Anywhere", Move, "10.AlterEgo_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
		ModifyUnitShields(All, " * Fenix", CurrentPlayer, "Anywhere", 1);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		Wait(230);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		Wait(230);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(AllPlayers, SetTo, 4301, " `SkillText2");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(4, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = true,
			intransit = false,
			hallucinated = false,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(4, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = true,
			intransit = false,
			hallucinated = false,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(4, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = true,
			intransit = false,
			hallucinated = false,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(4, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = true,
			intransit = false,
			hallucinated = false,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		Wait(230);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Wait(500);
		MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "Anywhere", "[Skill]Unit_Wait_ALL");
		Wait(300);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(1000);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}
