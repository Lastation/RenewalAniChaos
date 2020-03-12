Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		Wait(3100);
		SetSwitch("Recall - Alther", Clear);
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x0000005C);
		SetMemory(0x58E80C, Add, 0x0000005C);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x0000005C);
		SetMemory(0x58E810, Subtract, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x0000005C);
		SetMemory(0x58E80C, Subtract, 0x0000005C);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Add, 0x0000005C);
		SetMemory(0x58E810, Add, 0x0000005C);
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x0000005C);
		SetMemory(0x58E810, Subtract, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x0000005C);
		SetMemory(0x58E80C, Subtract, 0x0000005C);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Add, 0x0000005C);
		SetMemory(0x58E810, Add, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x0000005C);
		SetMemory(0x58E80C, Add, 0x0000005C);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x0000005C);
		SetMemory(0x58E810, Subtract, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x0000005C);
		SetMemory(0x58E80C, Subtract, 0x0000005C);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x0000005C);
		SetMemory(0x58E810, Add, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x0000005C);
		SetMemory(0x58E80C, Add, 0x0000005C);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x0000005C);
		SetMemory(0x58E80C, Add, 0x0000005C);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x0000005C);
		SetMemory(0x58E810, Subtract, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x0000005C);
		SetMemory(0x58E80C, Subtract, 0x0000005C);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x0000005C);
		SetMemory(0x58E810, Add, 0x0000005C);
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000E0);
		SetMemory(0x58E810, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000E0);
		SetMemory(0x58E80C, Subtract, 0x000000E0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000E0);
		SetMemory(0x58E810, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000E0);
		SetMemory(0x58E80C, Add, 0x000000E0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		Order("120 + 1n Archon", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		Wait(1500);
		SetDeaths(AllPlayers, SetTo, 10001, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Polarlicht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		ModifyUnitHangarCount(2, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
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
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Gantrithor", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(90);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 13, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Gantrithor", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		ModifyUnitHangarCount(2, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(90);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 149, " `UltimateCoolTime");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Bring(CurrentPlayer, AtMost, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 150, " `UltimateCoolTime");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Subtract, 150, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 330, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 10010, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(1000);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		Wait(1000);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
	},
}
