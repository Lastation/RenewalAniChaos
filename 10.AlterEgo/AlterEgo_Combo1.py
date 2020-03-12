Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
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
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
		Wait(1200);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop2");
		Wait(600);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		Wait(1000);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}