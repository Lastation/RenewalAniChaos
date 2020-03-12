Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
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
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		ModifyUnitHangarCount(1, All, " Unit. Polarlicht", CurrentPlayer, "Anywhere");
		Wait(230);
		KillUnitAt(All, " Unit. Polarlicht", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("60 + 1n Dragoon", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("60 + 1n Dragoon", CurrentPlayer, "Anywhere", Attack, "10.AlterEgo");
		Wait(1700);
		SetDeaths(AllPlayers, SetTo, 4201, " `SkillText2");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Subtract, 0x00000060);
		SetMemory(0x58E810, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000060);
		SetMemory(0x58E80C, Subtract, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000060);
		SetMemory(0x58E80C, Add, 0x00000060);
		SetMemory(0x58E808, Add, 0x00000060);
		SetMemory(0x58E810, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000A0);
		SetMemory(0x58E80C, Add, 0x000000A0);
		SetMemory(0x58E808, Subtract, 0x00000020);
		SetMemory(0x58E810, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000020);
		SetMemory(0x58E80C, Subtract, 0x00000020);
		SetMemory(0x58E808, Subtract, 0x000000A0);
		SetMemory(0x58E810, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000A0);
		SetMemory(0x58E80C, Subtract, 0x000000A0);
		SetMemory(0x58E808, Add, 0x00000020);
		SetMemory(0x58E810, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000020);
		SetMemory(0x58E80C, Add, 0x00000020);
		SetMemory(0x58E808, Add, 0x000000A0);
		SetMemory(0x58E810, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(9, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Unit. Polarlicht", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(1, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, " Unit. Polarlicht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000100);
		SetMemory(0x58E80C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Subtract, 0x00000100);
		SetMemory(0x58E810, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000100);
		SetMemory(0x58E80C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E808, Add, 0x00000100);
		SetMemory(0x58E810, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Subtract, 0x00000080);
		SetMemory(0x58E810, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000080);
		SetMemory(0x58E80C, Subtract, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000080);
		SetMemory(0x58E80C, Add, 0x00000080);
		SetMemory(0x58E808, Add, 0x00000080);
		SetMemory(0x58E810, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x000000C0);
		SetMemory(0x58E80C, Add, 0x000000C0);
		SetMemory(0x58E808, Subtract, 0x00000040);
		SetMemory(0x58E810, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x00000040);
		SetMemory(0x58E80C, Subtract, 0x00000040);
		SetMemory(0x58E808, Subtract, 0x000000C0);
		SetMemory(0x58E810, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Subtract, 0x000000C0);
		SetMemory(0x58E80C, Subtract, 0x000000C0);
		SetMemory(0x58E808, Add, 0x00000040);
		SetMemory(0x58E810, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E804, Add, 0x00000040);
		SetMemory(0x58E80C, Add, 0x00000040);
		SetMemory(0x58E808, Add, 0x000000C0);
		SetMemory(0x58E810, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveUnit(8, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "10.AlterEgo");
		MoveLocation("10.AlterEgo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Wait(0);
		ModifyUnitHangarCount(1, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");
		SetDeaths(AllPlayers, SetTo, 4202, " `SkillText2");
		Wait(1800);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Bring(CurrentPlayer, AtMost, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 220, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 4300, " `SkillText2");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		Wait(1000);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}