Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		MoveUnit(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveLocation("01.Rusaruka_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "01.Rusaruka_Bozo");
		MoveUnit(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		RemoveUnit("Protoss Observer", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetSwitch("Recall - Rusalka", Set);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(800);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(50);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "01.Rusaruka", CurrentPlayer);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000E0);
		SetMemory(0x58DECC, Add, 0x000000E0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000E0);
		SetMemory(0x58DED8, Add, 0x000000E0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000E0);
		SetMemory(0x58DECC, Subtract, 0x000000E0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000E0);
		SetMemory(0x58DED8, Subtract, 0x000000E0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Guardian", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(130);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Guardian", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(130);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		SetSwitch("Recall - Rusalka", Clear);
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("01.Rusaruka_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "01.Rusaruka_Bozo");
		MoveUnit(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		RemoveUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetSwitch("Recall - Rusalka", Set);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000100);
		SetMemory(0x58DECC, Add, 0x00000100);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000100);
		SetMemory(0x58DED8, Add, 0x00000100);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000100);
		SetMemory(0x58DECC, Subtract, 0x00000100);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000100);
		SetMemory(0x58DED8, Subtract, 0x00000100);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000140);
		SetMemory(0x58DECC, Add, 0x00000140);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000140);
		SetMemory(0x58DED8, Add, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000140);
		SetMemory(0x58DECC, Subtract, 0x00000140);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000140);
		SetMemory(0x58DED8, Subtract, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000100);
		SetMemory(0x58DECC, Add, 0x00000100);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000100);
		SetMemory(0x58DED8, Add, 0x00000100);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000100);
		SetMemory(0x58DECC, Subtract, 0x00000100);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000100);
		SetMemory(0x58DED8, Subtract, 0x00000100);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000100);
		SetMemory(0x58DED8, Add, 0x00000100);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000100);
		SetMemory(0x58DECC, Subtract, 0x00000100);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000100);
		SetMemory(0x58DED8, Subtract, 0x00000100);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000100);
		SetMemory(0x58DECC, Add, 0x00000100);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000140);
		SetMemory(0x58DED8, Add, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000140);
		SetMemory(0x58DECC, Subtract, 0x00000140);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000140);
		SetMemory(0x58DED8, Subtract, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000140);
		SetMemory(0x58DECC, Add, 0x00000140);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 6, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000140);
		SetMemory(0x58DED8, Add, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000140);
		SetMemory(0x58DECC, Subtract, 0x00000140);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000140);
		SetMemory(0x58DED8, Subtract, 0x00000140);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000140);
		SetMemory(0x58DECC, Add, 0x00000140);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(2000);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillStep");
		Wait(500);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("Recall - Rusalka", Clear);
	},
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 16, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 33, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		MoveUnit(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 25, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 33, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		MoveUnit(All, "80 + 1n Mutalisk", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetSwitch("Recall - Rusalka", Set);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000050);
		SetMemory(0x58DECC, Add, 0x00000050);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000050);
		SetMemory(0x58DED8, Add, 0x00000050);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000050);
		SetMemory(0x58DECC, Subtract, 0x00000050);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000050);
		SetMemory(0x58DED8, Subtract, 0x00000050);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000038);
		SetMemory(0x58DECC, Add, 0x00000038);
		SetMemory(0x58DED0, Add, 0x00000038);
		SetMemory(0x58DED8, Add, 0x00000038);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000038);
		SetMemory(0x58DECC, Subtract, 0x00000038);
		SetMemory(0x58DED0, Add, 0x00000038);
		SetMemory(0x58DED8, Add, 0x00000038);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000038);
		SetMemory(0x58DECC, Subtract, 0x00000038);
		SetMemory(0x58DED0, Subtract, 0x00000038);
		SetMemory(0x58DED8, Subtract, 0x00000038);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000038);
		SetMemory(0x58DECC, Add, 0x00000038);
		SetMemory(0x58DED0, Subtract, 0x00000038);
		SetMemory(0x58DED8, Subtract, 0x00000038);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A0);
		SetMemory(0x58DECC, Add, 0x000000A0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000A0);
		SetMemory(0x58DED8, Add, 0x000000A0);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A0);
		SetMemory(0x58DECC, Subtract, 0x000000A0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000A0);
		SetMemory(0x58DED8, Subtract, 0x000000A0);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Add, 0x00000072);
		SetMemory(0x58DED8, Add, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000072);
		SetMemory(0x58DECC, Subtract, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000072);
		SetMemory(0x58DECC, Add, 0x00000072);
		SetMemory(0x58DED0, Subtract, 0x00000072);
		SetMemory(0x58DED8, Subtract, 0x00000072);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000120);
		SetMemory(0x58DECC, Add, 0x00000120);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000120);
		SetMemory(0x58DED8, Add, 0x00000120);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000120);
		SetMemory(0x58DECC, Subtract, 0x00000120);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000120);
		SetMemory(0x58DED8, Subtract, 0x00000120);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000032);
		SetMemory(0x58DECC, Add, 0x00000032);
		SetMemory(0x58DED0, Add, 0x0000011C);
		SetMemory(0x58DED8, Add, 0x0000011C);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000011C);
		SetMemory(0x58DECC, Subtract, 0x0000011C);
		SetMemory(0x58DED0, Add, 0x00000032);
		SetMemory(0x58DED8, Add, 0x00000032);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000032);
		SetMemory(0x58DECC, Subtract, 0x00000032);
		SetMemory(0x58DED0, Subtract, 0x0000011C);
		SetMemory(0x58DED8, Subtract, 0x0000011C);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000011C);
		SetMemory(0x58DECC, Add, 0x0000011C);
		SetMemory(0x58DED0, Subtract, 0x00000032);
		SetMemory(0x58DED8, Subtract, 0x00000032);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000062);
		SetMemory(0x58DECC, Add, 0x00000062);
		SetMemory(0x58DED0, Add, 0x0000010E);
		SetMemory(0x58DED8, Add, 0x0000010E);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000010E);
		SetMemory(0x58DECC, Subtract, 0x0000010E);
		SetMemory(0x58DED0, Add, 0x00000062);
		SetMemory(0x58DED8, Add, 0x00000062);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000062);
		SetMemory(0x58DECC, Subtract, 0x00000062);
		SetMemory(0x58DED0, Subtract, 0x0000010E);
		SetMemory(0x58DED8, Subtract, 0x0000010E);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000010E);
		SetMemory(0x58DECC, Add, 0x0000010E);
		SetMemory(0x58DED0, Subtract, 0x00000062);
		SetMemory(0x58DED8, Subtract, 0x00000062);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000090);
		SetMemory(0x58DECC, Add, 0x00000090);
		SetMemory(0x58DED0, Add, 0x000000F9);
		SetMemory(0x58DED8, Add, 0x000000F9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F9);
		SetMemory(0x58DECC, Subtract, 0x000000F9);
		SetMemory(0x58DED0, Add, 0x00000090);
		SetMemory(0x58DED8, Add, 0x00000090);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000090);
		SetMemory(0x58DECC, Subtract, 0x00000090);
		SetMemory(0x58DED0, Subtract, 0x000000F9);
		SetMemory(0x58DED8, Subtract, 0x000000F9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F9);
		SetMemory(0x58DECC, Add, 0x000000F9);
		SetMemory(0x58DED0, Subtract, 0x00000090);
		SetMemory(0x58DED8, Subtract, 0x00000090);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000B9);
		SetMemory(0x58DECC, Add, 0x000000B9);
		SetMemory(0x58DED0, Add, 0x000000DC);
		SetMemory(0x58DED8, Add, 0x000000DC);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DC);
		SetMemory(0x58DECC, Subtract, 0x000000DC);
		SetMemory(0x58DED0, Add, 0x000000B9);
		SetMemory(0x58DED8, Add, 0x000000B9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000B9);
		SetMemory(0x58DECC, Subtract, 0x000000B9);
		SetMemory(0x58DED0, Subtract, 0x000000DC);
		SetMemory(0x58DED8, Subtract, 0x000000DC);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DC);
		SetMemory(0x58DECC, Add, 0x000000DC);
		SetMemory(0x58DED0, Subtract, 0x000000B9);
		SetMemory(0x58DED8, Subtract, 0x000000B9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DC);
		SetMemory(0x58DECC, Add, 0x000000DC);
		SetMemory(0x58DED0, Add, 0x000000B9);
		SetMemory(0x58DED8, Add, 0x000000B9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000B9);
		SetMemory(0x58DECC, Subtract, 0x000000B9);
		SetMemory(0x58DED0, Add, 0x000000DC);
		SetMemory(0x58DED8, Add, 0x000000DC);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DC);
		SetMemory(0x58DECC, Subtract, 0x000000DC);
		SetMemory(0x58DED0, Subtract, 0x000000B9);
		SetMemory(0x58DED8, Subtract, 0x000000B9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000B9);
		SetMemory(0x58DECC, Add, 0x000000B9);
		SetMemory(0x58DED0, Subtract, 0x000000DC);
		SetMemory(0x58DED8, Subtract, 0x000000DC);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F9);
		SetMemory(0x58DECC, Add, 0x000000F9);
		SetMemory(0x58DED0, Add, 0x00000090);
		SetMemory(0x58DED8, Add, 0x00000090);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000090);
		SetMemory(0x58DECC, Subtract, 0x00000090);
		SetMemory(0x58DED0, Add, 0x000000F9);
		SetMemory(0x58DED8, Add, 0x000000F9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F9);
		SetMemory(0x58DECC, Subtract, 0x000000F9);
		SetMemory(0x58DED0, Subtract, 0x00000090);
		SetMemory(0x58DED8, Subtract, 0x00000090);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000090);
		SetMemory(0x58DECC, Add, 0x00000090);
		SetMemory(0x58DED0, Subtract, 0x000000F9);
		SetMemory(0x58DED8, Subtract, 0x000000F9);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000010E);
		SetMemory(0x58DECC, Add, 0x0000010E);
		SetMemory(0x58DED0, Add, 0x00000062);
		SetMemory(0x58DED8, Add, 0x00000062);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000062);
		SetMemory(0x58DECC, Subtract, 0x00000062);
		SetMemory(0x58DED0, Add, 0x0000010E);
		SetMemory(0x58DED8, Add, 0x0000010E);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000010E);
		SetMemory(0x58DECC, Subtract, 0x0000010E);
		SetMemory(0x58DED0, Subtract, 0x00000062);
		SetMemory(0x58DED8, Subtract, 0x00000062);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000062);
		SetMemory(0x58DECC, Add, 0x00000062);
		SetMemory(0x58DED0, Subtract, 0x0000010E);
		SetMemory(0x58DED8, Subtract, 0x0000010E);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000011C);
		SetMemory(0x58DECC, Add, 0x0000011C);
		SetMemory(0x58DED0, Add, 0x00000032);
		SetMemory(0x58DED8, Add, 0x00000032);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000032);
		SetMemory(0x58DECC, Subtract, 0x00000032);
		SetMemory(0x58DED0, Add, 0x0000011C);
		SetMemory(0x58DED8, Add, 0x0000011C);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000011C);
		SetMemory(0x58DECC, Subtract, 0x0000011C);
		SetMemory(0x58DED0, Subtract, 0x00000032);
		SetMemory(0x58DED8, Subtract, 0x00000032);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000032);
		SetMemory(0x58DECC, Add, 0x00000032);
		SetMemory(0x58DED0, Subtract, 0x0000011C);
		SetMemory(0x58DED8, Subtract, 0x0000011C);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 3, " `SkillCount");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000100);
		SetMemory(0x58DECC, Add, 0x00000100);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000100);
		SetMemory(0x58DED8, Add, 0x00000100);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000100);
		SetMemory(0x58DECC, Subtract, 0x00000100);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000100);
		SetMemory(0x58DED8, Subtract, 0x00000100);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000FC);
		SetMemory(0x58DECC, Add, 0x000000FC);
		SetMemory(0x58DED0, Add, 0x0000002C);
		SetMemory(0x58DED8, Add, 0x0000002C);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000002C);
		SetMemory(0x58DECC, Subtract, 0x0000002C);
		SetMemory(0x58DED0, Add, 0x000000FC);
		SetMemory(0x58DED8, Add, 0x000000FC);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000FC);
		SetMemory(0x58DECC, Subtract, 0x000000FC);
		SetMemory(0x58DED0, Subtract, 0x0000002C);
		SetMemory(0x58DED8, Subtract, 0x0000002C);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000002C);
		SetMemory(0x58DECC, Add, 0x0000002C);
		SetMemory(0x58DED0, Subtract, 0x000000FC);
		SetMemory(0x58DED8, Subtract, 0x000000FC);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F0);
		SetMemory(0x58DECC, Add, 0x000000F0);
		SetMemory(0x58DED0, Add, 0x00000058);
		SetMemory(0x58DED8, Add, 0x00000058);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000058);
		SetMemory(0x58DECC, Subtract, 0x00000058);
		SetMemory(0x58DED0, Add, 0x000000F0);
		SetMemory(0x58DED8, Add, 0x000000F0);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F0);
		SetMemory(0x58DECC, Subtract, 0x000000F0);
		SetMemory(0x58DED0, Subtract, 0x00000058);
		SetMemory(0x58DED8, Subtract, 0x00000058);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000058);
		SetMemory(0x58DECC, Add, 0x00000058);
		SetMemory(0x58DED0, Subtract, 0x000000F0);
		SetMemory(0x58DED8, Subtract, 0x000000F0);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DE);
		SetMemory(0x58DECC, Add, 0x000000DE);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000DE);
		SetMemory(0x58DED8, Add, 0x000000DE);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DE);
		SetMemory(0x58DECC, Subtract, 0x000000DE);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000DE);
		SetMemory(0x58DED8, Subtract, 0x000000DE);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C4);
		SetMemory(0x58DECC, Add, 0x000000C4);
		SetMemory(0x58DED0, Add, 0x000000A5);
		SetMemory(0x58DED8, Add, 0x000000A5);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A5);
		SetMemory(0x58DECC, Subtract, 0x000000A5);
		SetMemory(0x58DED0, Add, 0x000000C4);
		SetMemory(0x58DED8, Add, 0x000000C4);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C4);
		SetMemory(0x58DECC, Subtract, 0x000000C4);
		SetMemory(0x58DED0, Subtract, 0x000000A5);
		SetMemory(0x58DED8, Subtract, 0x000000A5);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A5);
		SetMemory(0x58DECC, Add, 0x000000A5);
		SetMemory(0x58DED0, Subtract, 0x000000C4);
		SetMemory(0x58DED8, Subtract, 0x000000C4);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000A5);
		SetMemory(0x58DECC, Add, 0x000000A5);
		SetMemory(0x58DED0, Add, 0x000000C4);
		SetMemory(0x58DED8, Add, 0x000000C4);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C4);
		SetMemory(0x58DECC, Subtract, 0x000000C4);
		SetMemory(0x58DED0, Add, 0x000000A5);
		SetMemory(0x58DED8, Add, 0x000000A5);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000A5);
		SetMemory(0x58DECC, Subtract, 0x000000A5);
		SetMemory(0x58DED0, Subtract, 0x000000C4);
		SetMemory(0x58DED8, Subtract, 0x000000C4);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C4);
		SetMemory(0x58DECC, Add, 0x000000C4);
		SetMemory(0x58DED0, Subtract, 0x000000A5);
		SetMemory(0x58DED8, Subtract, 0x000000A5);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000DE);
		SetMemory(0x58DED8, Add, 0x000000DE);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DE);
		SetMemory(0x58DECC, Subtract, 0x000000DE);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000DE);
		SetMemory(0x58DED8, Subtract, 0x000000DE);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DE);
		SetMemory(0x58DECC, Add, 0x000000DE);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000058);
		SetMemory(0x58DECC, Add, 0x00000058);
		SetMemory(0x58DED0, Add, 0x000000F0);
		SetMemory(0x58DED8, Add, 0x000000F0);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F0);
		SetMemory(0x58DECC, Subtract, 0x000000F0);
		SetMemory(0x58DED0, Add, 0x00000058);
		SetMemory(0x58DED8, Add, 0x00000058);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000058);
		SetMemory(0x58DECC, Subtract, 0x00000058);
		SetMemory(0x58DED0, Subtract, 0x000000F0);
		SetMemory(0x58DED8, Subtract, 0x000000F0);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F0);
		SetMemory(0x58DECC, Add, 0x000000F0);
		SetMemory(0x58DED0, Subtract, 0x00000058);
		SetMemory(0x58DED8, Subtract, 0x00000058);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000002C);
		SetMemory(0x58DECC, Add, 0x0000002C);
		SetMemory(0x58DED0, Add, 0x000000FC);
		SetMemory(0x58DED8, Add, 0x000000FC);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000FC);
		SetMemory(0x58DECC, Subtract, 0x000000FC);
		SetMemory(0x58DED0, Add, 0x0000002C);
		SetMemory(0x58DED8, Add, 0x0000002C);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000002C);
		SetMemory(0x58DECC, Subtract, 0x0000002C);
		SetMemory(0x58DED0, Subtract, 0x000000FC);
		SetMemory(0x58DED8, Subtract, 0x000000FC);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000FC);
		SetMemory(0x58DECC, Add, 0x000000FC);
		SetMemory(0x58DED0, Subtract, 0x0000002C);
		SetMemory(0x58DED8, Subtract, 0x0000002C);
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 14, " `SkillCount");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000120);
		SetMemory(0x58DECC, Add, 0x00000120);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000120);
		SetMemory(0x58DED8, Add, 0x00000120);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000120);
		SetMemory(0x58DECC, Subtract, 0x00000120);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000120);
		SetMemory(0x58DED8, Subtract, 0x00000120);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000032);
		SetMemory(0x58DECC, Add, 0x00000032);
		SetMemory(0x58DED0, Add, 0x0000011C);
		SetMemory(0x58DED8, Add, 0x0000011C);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000011C);
		SetMemory(0x58DECC, Subtract, 0x0000011C);
		SetMemory(0x58DED0, Add, 0x00000032);
		SetMemory(0x58DED8, Add, 0x00000032);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000032);
		SetMemory(0x58DECC, Subtract, 0x00000032);
		SetMemory(0x58DED0, Subtract, 0x0000011C);
		SetMemory(0x58DED8, Subtract, 0x0000011C);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000011C);
		SetMemory(0x58DECC, Add, 0x0000011C);
		SetMemory(0x58DED0, Subtract, 0x00000032);
		SetMemory(0x58DED8, Subtract, 0x00000032);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000062);
		SetMemory(0x58DECC, Add, 0x00000062);
		SetMemory(0x58DED0, Add, 0x0000010E);
		SetMemory(0x58DED8, Add, 0x0000010E);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000010E);
		SetMemory(0x58DECC, Subtract, 0x0000010E);
		SetMemory(0x58DED0, Add, 0x00000062);
		SetMemory(0x58DED8, Add, 0x00000062);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000062);
		SetMemory(0x58DECC, Subtract, 0x00000062);
		SetMemory(0x58DED0, Subtract, 0x0000010E);
		SetMemory(0x58DED8, Subtract, 0x0000010E);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000010E);
		SetMemory(0x58DECC, Add, 0x0000010E);
		SetMemory(0x58DED0, Subtract, 0x00000062);
		SetMemory(0x58DED8, Subtract, 0x00000062);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000090);
		SetMemory(0x58DECC, Add, 0x00000090);
		SetMemory(0x58DED0, Add, 0x000000F9);
		SetMemory(0x58DED8, Add, 0x000000F9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F9);
		SetMemory(0x58DECC, Subtract, 0x000000F9);
		SetMemory(0x58DED0, Add, 0x00000090);
		SetMemory(0x58DED8, Add, 0x00000090);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000090);
		SetMemory(0x58DECC, Subtract, 0x00000090);
		SetMemory(0x58DED0, Subtract, 0x000000F9);
		SetMemory(0x58DED8, Subtract, 0x000000F9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F9);
		SetMemory(0x58DECC, Add, 0x000000F9);
		SetMemory(0x58DED0, Subtract, 0x00000090);
		SetMemory(0x58DED8, Subtract, 0x00000090);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000B9);
		SetMemory(0x58DECC, Add, 0x000000B9);
		SetMemory(0x58DED0, Add, 0x000000DC);
		SetMemory(0x58DED8, Add, 0x000000DC);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DC);
		SetMemory(0x58DECC, Subtract, 0x000000DC);
		SetMemory(0x58DED0, Add, 0x000000B9);
		SetMemory(0x58DED8, Add, 0x000000B9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000B9);
		SetMemory(0x58DECC, Subtract, 0x000000B9);
		SetMemory(0x58DED0, Subtract, 0x000000DC);
		SetMemory(0x58DED8, Subtract, 0x000000DC);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DC);
		SetMemory(0x58DECC, Add, 0x000000DC);
		SetMemory(0x58DED0, Subtract, 0x000000B9);
		SetMemory(0x58DED8, Subtract, 0x000000B9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000DC);
		SetMemory(0x58DECC, Add, 0x000000DC);
		SetMemory(0x58DED0, Add, 0x000000B9);
		SetMemory(0x58DED8, Add, 0x000000B9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000B9);
		SetMemory(0x58DECC, Subtract, 0x000000B9);
		SetMemory(0x58DED0, Add, 0x000000DC);
		SetMemory(0x58DED8, Add, 0x000000DC);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000DC);
		SetMemory(0x58DECC, Subtract, 0x000000DC);
		SetMemory(0x58DED0, Subtract, 0x000000B9);
		SetMemory(0x58DED8, Subtract, 0x000000B9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000B9);
		SetMemory(0x58DECC, Add, 0x000000B9);
		SetMemory(0x58DED0, Subtract, 0x000000DC);
		SetMemory(0x58DED8, Subtract, 0x000000DC);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000F9);
		SetMemory(0x58DECC, Add, 0x000000F9);
		SetMemory(0x58DED0, Add, 0x00000090);
		SetMemory(0x58DED8, Add, 0x00000090);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000090);
		SetMemory(0x58DECC, Subtract, 0x00000090);
		SetMemory(0x58DED0, Add, 0x000000F9);
		SetMemory(0x58DED8, Add, 0x000000F9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000F9);
		SetMemory(0x58DECC, Subtract, 0x000000F9);
		SetMemory(0x58DED0, Subtract, 0x00000090);
		SetMemory(0x58DED8, Subtract, 0x00000090);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000090);
		SetMemory(0x58DECC, Add, 0x00000090);
		SetMemory(0x58DED0, Subtract, 0x000000F9);
		SetMemory(0x58DED8, Subtract, 0x000000F9);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000010E);
		SetMemory(0x58DECC, Add, 0x0000010E);
		SetMemory(0x58DED0, Add, 0x00000062);
		SetMemory(0x58DED8, Add, 0x00000062);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000062);
		SetMemory(0x58DECC, Subtract, 0x00000062);
		SetMemory(0x58DED0, Add, 0x0000010E);
		SetMemory(0x58DED8, Add, 0x0000010E);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000010E);
		SetMemory(0x58DECC, Subtract, 0x0000010E);
		SetMemory(0x58DED0, Subtract, 0x00000062);
		SetMemory(0x58DED8, Subtract, 0x00000062);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000062);
		SetMemory(0x58DECC, Add, 0x00000062);
		SetMemory(0x58DED0, Subtract, 0x0000010E);
		SetMemory(0x58DED8, Subtract, 0x0000010E);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 32, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x0000011C);
		SetMemory(0x58DECC, Add, 0x0000011C);
		SetMemory(0x58DED0, Add, 0x00000032);
		SetMemory(0x58DED8, Add, 0x00000032);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000032);
		SetMemory(0x58DECC, Subtract, 0x00000032);
		SetMemory(0x58DED0, Add, 0x0000011C);
		SetMemory(0x58DED8, Add, 0x0000011C);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x0000011C);
		SetMemory(0x58DECC, Subtract, 0x0000011C);
		SetMemory(0x58DED0, Subtract, 0x00000032);
		SetMemory(0x58DED8, Subtract, 0x00000032);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000032);
		SetMemory(0x58DECC, Add, 0x00000032);
		SetMemory(0x58DED0, Subtract, 0x0000011C);
		SetMemory(0x58DED8, Subtract, 0x0000011C);
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(50);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 24, " `SkillCount");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetSwitch("Recall - Rusalka", Clear);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 34, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		GiveUnits(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "80 + 1n Mutalisk", CurrentPlayer, "Anywhere", P7);
		Wait(0);
		SetSwitch("JunkYardDog", Set);
		SetDeaths(AllPlayers, SetTo, 1301, " `SkillText_Uiltimate");
		Wait(1200);
		GiveUnits(All, "80 + 1n Tom Kazansky", P7, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Artanis", P7, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Mutalisk", P7, "Anywhere", CurrentPlayer);
		SetSwitch("JunkYardDog", Clear);
		Wait(0);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(2600);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 34, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		GiveUnits(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "80 + 1n Mutalisk", CurrentPlayer, "Anywhere", P8);
		Wait(0);
		SetSwitch("JunkYardDog", Set);
		SetDeaths(AllPlayers, SetTo, 1301, " `SkillText");
		Wait(1200);
		GiveUnits(All, "80 + 1n Tom Kazansky", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Artanis", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Mutalisk", P8, "Anywhere", CurrentPlayer);
		SetSwitch("JunkYardDog", Clear);
		Wait(0);
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Order("80 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(2600);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 35, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 36, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 37, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 38, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000100);
		SetMemory(0x58DECC, Add, 0x00000100);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000100);
		SetMemory(0x58DED8, Add, 0x00000100);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000100);
		SetMemory(0x58DECC, Subtract, 0x00000100);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000100);
		SetMemory(0x58DED8, Subtract, 0x00000100);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 39, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000140);
		SetMemory(0x58DECC, Add, 0x00000140);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000140);
		SetMemory(0x58DED8, Add, 0x00000140);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000140);
		SetMemory(0x58DECC, Subtract, 0x00000140);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000140);
		SetMemory(0x58DED8, Subtract, 0x00000140);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 40, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 41, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 42, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 43, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 44, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 45, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "01.Rusaruka");
		Wait(1200);
		KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 46, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("UiltimateSwitch", Clear);
	},
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Unique
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, AtMost, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveUnit(All, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Unique]Position_Team1");
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveUnit(All, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Unique]Position_Team2");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 1400, " `SkillText_Unique");
		Wait(5800);
		SetDeaths(AllPlayers, SetTo, 1401, " `SkillText_Unique");
		Wait(5600);
		SetDeaths(AllPlayers, SetTo, 1402, " `SkillText_Unique");
		Wait(6100);
		SetDeaths(AllPlayers, SetTo, 1403, " `SkillText_Unique");
		Wait(6200);
		SetDeaths(AllPlayers, SetTo, 1404, " `SkillText_Unique");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Add, 0x00000020);
		SetMemory(0x58DED8, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000020);
		SetMemory(0x58DECC, Subtract, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000020);
		SetMemory(0x58DECC, Add, 0x00000020);
		SetMemory(0x58DED0, Subtract, 0x00000020);
		SetMemory(0x58DED8, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000080);
		SetMemory(0x58DECC, Add, 0x00000080);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000080);
		SetMemory(0x58DED8, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000080);
		SetMemory(0x58DECC, Subtract, 0x00000080);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000080);
		SetMemory(0x58DED8, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000040);
		SetMemory(0x58DECC, Add, 0x00000040);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000040);
		SetMemory(0x58DED8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000040);
		SetMemory(0x58DECC, Subtract, 0x00000040);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000040);
		SetMemory(0x58DED8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x000000C0);
		SetMemory(0x58DECC, Add, 0x000000C0);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x000000C0);
		SetMemory(0x58DED8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x000000C0);
		SetMemory(0x58DECC, Subtract, 0x000000C0);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x000000C0);
		SetMemory(0x58DED8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000060);
		SetMemory(0x58DECC, Add, 0x00000060);
		SetMemory(0x58DED0, Add, 0x00000000);
		SetMemory(0x58DED8, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000000);
		SetMemory(0x58DECC, Subtract, 0x00000000);
		SetMemory(0x58DED0, Add, 0x00000060);
		SetMemory(0x58DED8, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Subtract, 0x00000060);
		SetMemory(0x58DECC, Subtract, 0x00000060);
		SetMemory(0x58DED0, Subtract, 0x00000000);
		SetMemory(0x58DED8, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		MoveLocation("01.Rusaruka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58DED4, Add, 0x00000000);
		SetMemory(0x58DECC, Add, 0x00000000);
		SetMemory(0x58DED0, Subtract, 0x00000060);
		SetMemory(0x58DED8, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "01.Rusaruka");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetInvincibility(Disable, " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Unique
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "Csejte Ungarn Nachtzehrer", "[Skill]Unit_Wait_8", P7);
		MoveUnit(1, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Potal]Base7");
		MoveUnit(1, "Csejte Ungarn Nachtzehrer", P7, "[Skill]Unit_Wait_ALL", "[Unique]Position_Team1");
		MoveUnit(1, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Unique]Position_Team1");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "Csejte Ungarn Nachtzehrer", "[Skill]Unit_Wait_8", P8);
		MoveUnit(1, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Potal]Base8");
		MoveUnit(1, "Csejte Ungarn Nachtzehrer", P8, "[Skill]Unit_Wait_ALL", "[Unique]Position_Team2");
		MoveUnit(1, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Unique]Position_Team2");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
	},
}