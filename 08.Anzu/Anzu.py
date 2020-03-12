

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 08.Anzu
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2001, " * Infested Kerrigan");
	},
	actions = {
		Comment("08.Anzu");
		SetDeaths(AllPlayers, SetTo, 8, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 2000, " * Infested Kerrigan");
		CreateUnit(1, " * Infested Kerrigan", "[Select]Select Unit", CurrentPlayer);
		SetInvincibility(Enable, "Men", CurrentPlayer, "[Select]Select Unit");
		PreserveTrigger();
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

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtMost, 24);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\x13\x17[ O Skill \x04은 25레벨 이상시에만 사용이 가능합니다. \x17]", 0);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Bring(CurrentPlayer, Exactly, 0, " * Infested Kerrigan", "[Potal]Shop7");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		MinimapPing("[Potal]Shop7");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Bring(CurrentPlayer, Exactly, 0, " * Infested Kerrigan", "[Potal]Shop7");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		MinimapPing("[Potal]Shop8");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "[Potal]Shop7");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 8000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 2880, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 120, " `UniqueSkill");
		SetDeaths(P1, Add, 20, " `UltimateCoolTime");
		SetDeaths(P2, Add, 20, " `UltimateCoolTime");
		SetDeaths(P3, Add, 20, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, Subtract, 20, " `UltimateCoolTime");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "[Potal]Shop8");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 8000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 2880, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 120, " `UniqueSkill");
		SetDeaths(P4, Add, 20, " `UltimateCoolTime");
		SetDeaths(P5, Add, 20, " `UltimateCoolTime");
		SetDeaths(P6, Add, 20, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, Subtract, 20, " `UltimateCoolTime");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 200, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 300, " `SkillStep");
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 100, " `SkillStep");
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
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

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 110, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2000, " `SkillText2");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2010, " `SkillText2");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 220, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2011, " `SkillText2");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 550, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Cleared);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 550, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 8000, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 550, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Set);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 700, Gas);
		PreserveTrigger();
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveUnit(All, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Potal]Shop7");
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveUnit(All, " * Infested Kerrigan", CurrentPlayer, "Anywhere", "[Potal]Shop8");
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
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

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(130);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(130);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
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

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000000);
		SetMemory(0x58E7AC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000000);
		SetMemory(0x58E7A8, Subtract, 0x00000000);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000000);
		SetMemory(0x58E7AC, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000000);
		SetMemory(0x58E7A8, Add, 0x00000000);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000000);
		SetMemory(0x58E7AC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000000);
		SetMemory(0x58E7A8, Subtract, 0x00000000);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000000);
		SetMemory(0x58E7AC, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000000);
		SetMemory(0x58E7A8, Add, 0x00000000);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		Wait(0);
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

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(1000);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(130);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "08.Anzu_Bozo");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(300);
		Disabled(KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer));
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(300);
		Disabled(KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer));
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(300);
		Disabled(KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer));
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(1000);
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "08.Anzu_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000031);
		SetMemory(0x58E7A8, Add, 0x00000031);
		SetMemory(0x58E7A4, Subtract, 0x00000076);
		SetMemory(0x58E7AC, Subtract, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000076);
		SetMemory(0x58E7A8, Add, 0x00000076);
		SetMemory(0x58E7A4, Add, 0x00000031);
		SetMemory(0x58E7AC, Add, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000031);
		SetMemory(0x58E7A8, Subtract, 0x00000031);
		SetMemory(0x58E7A4, Add, 0x00000076);
		SetMemory(0x58E7AC, Add, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000076);
		SetMemory(0x58E7A8, Subtract, 0x00000076);
		SetMemory(0x58E7A4, Subtract, 0x00000031);
		SetMemory(0x58E7AC, Subtract, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x0000005B);
		SetMemory(0x58E7A8, Add, 0x0000005B);
		SetMemory(0x58E7A4, Subtract, 0x0000005B);
		SetMemory(0x58E7AC, Subtract, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x0000005B);
		SetMemory(0x58E7A8, Add, 0x0000005B);
		SetMemory(0x58E7A4, Add, 0x0000005B);
		SetMemory(0x58E7AC, Add, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x0000005B);
		SetMemory(0x58E7A8, Subtract, 0x0000005B);
		SetMemory(0x58E7A4, Add, 0x0000005B);
		SetMemory(0x58E7AC, Add, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x0000005B);
		SetMemory(0x58E7A8, Subtract, 0x0000005B);
		SetMemory(0x58E7A4, Subtract, 0x0000005B);
		SetMemory(0x58E7AC, Subtract, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000076);
		SetMemory(0x58E7A8, Add, 0x00000076);
		SetMemory(0x58E7A4, Subtract, 0x00000031);
		SetMemory(0x58E7AC, Subtract, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000031);
		SetMemory(0x58E7A8, Add, 0x00000031);
		SetMemory(0x58E7A4, Add, 0x00000076);
		SetMemory(0x58E7AC, Add, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000076);
		SetMemory(0x58E7A8, Subtract, 0x00000076);
		SetMemory(0x58E7A4, Add, 0x00000031);
		SetMemory(0x58E7AC, Add, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000031);
		SetMemory(0x58E7A8, Subtract, 0x00000031);
		SetMemory(0x58E7A4, Subtract, 0x00000076);
		SetMemory(0x58E7AC, Subtract, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000076);
		SetMemory(0x58E7A8, Add, 0x00000076);
		SetMemory(0x58E7A4, Add, 0x00000031);
		SetMemory(0x58E7AC, Add, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000031);
		SetMemory(0x58E7A8, Subtract, 0x00000031);
		SetMemory(0x58E7A4, Add, 0x00000076);
		SetMemory(0x58E7AC, Add, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000076);
		SetMemory(0x58E7A8, Subtract, 0x00000076);
		SetMemory(0x58E7A4, Subtract, 0x00000031);
		SetMemory(0x58E7AC, Subtract, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000031);
		SetMemory(0x58E7A8, Add, 0x00000031);
		SetMemory(0x58E7A4, Subtract, 0x00000076);
		SetMemory(0x58E7AC, Subtract, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x0000005B);
		SetMemory(0x58E7A8, Add, 0x0000005B);
		SetMemory(0x58E7A4, Add, 0x0000005B);
		SetMemory(0x58E7AC, Add, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x0000005B);
		SetMemory(0x58E7A8, Subtract, 0x0000005B);
		SetMemory(0x58E7A4, Add, 0x0000005B);
		SetMemory(0x58E7AC, Add, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x0000005B);
		SetMemory(0x58E7A8, Subtract, 0x0000005B);
		SetMemory(0x58E7A4, Subtract, 0x0000005B);
		SetMemory(0x58E7AC, Subtract, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x0000005B);
		SetMemory(0x58E7A8, Add, 0x0000005B);
		SetMemory(0x58E7A4, Subtract, 0x0000005B);
		SetMemory(0x58E7AC, Subtract, 0x0000005B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000031);
		SetMemory(0x58E7A8, Add, 0x00000031);
		SetMemory(0x58E7A4, Add, 0x00000076);
		SetMemory(0x58E7AC, Add, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000076);
		SetMemory(0x58E7A8, Subtract, 0x00000076);
		SetMemory(0x58E7A4, Add, 0x00000031);
		SetMemory(0x58E7AC, Add, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000031);
		SetMemory(0x58E7A8, Subtract, 0x00000031);
		SetMemory(0x58E7A4, Subtract, 0x00000076);
		SetMemory(0x58E7AC, Subtract, 0x00000076);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000076);
		SetMemory(0x58E7A8, Add, 0x00000076);
		SetMemory(0x58E7A4, Subtract, 0x00000031);
		SetMemory(0x58E7AC, Subtract, 0x00000031);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		Wait(0);
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

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "08.Anzu_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000020);
		SetMemory(0x58E7A8, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000020);
		SetMemory(0x58E7AC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000020);
		SetMemory(0x58E7A8, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000020);
		SetMemory(0x58E7AC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000060);
		SetMemory(0x58E7A8, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000060);
		SetMemory(0x58E7AC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000060);
		SetMemory(0x58E7A8, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000060);
		SetMemory(0x58E7AC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000A0);
		SetMemory(0x58E7A8, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x000000A0);
		SetMemory(0x58E7AC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000A0);
		SetMemory(0x58E7A8, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x000000A0);
		SetMemory(0x58E7AC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000E0);
		SetMemory(0x58E7A8, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x000000E0);
		SetMemory(0x58E7AC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000E0);
		SetMemory(0x58E7A8, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x000000E0);
		SetMemory(0x58E7AC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000120);
		SetMemory(0x58E7A8, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Subtract, 0x00000120);
		SetMemory(0x58E7AC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000120);
		SetMemory(0x58E7A8, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A4, Add, 0x00000120);
		SetMemory(0x58E7AC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000020);
		SetMemory(0x58E7AC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000020);
		SetMemory(0x58E7A8, Subtract, 0x00000020);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000020);
		SetMemory(0x58E7AC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000020);
		SetMemory(0x58E7A8, Add, 0x00000020);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000E0);
		SetMemory(0x58E7A8, Add, 0x000000E0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000E0);
		SetMemory(0x58E7AC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000E0);
		SetMemory(0x58E7A8, Subtract, 0x000000E0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000E0);
		SetMemory(0x58E7AC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000060);
		SetMemory(0x58E7AC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000060);
		SetMemory(0x58E7A8, Subtract, 0x00000060);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000060);
		SetMemory(0x58E7AC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000060);
		SetMemory(0x58E7A8, Add, 0x00000060);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000A0);
		SetMemory(0x58E7A8, Add, 0x000000A0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000A0);
		SetMemory(0x58E7AC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000A0);
		SetMemory(0x58E7A8, Subtract, 0x000000A0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000A0);
		SetMemory(0x58E7AC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000080);
		SetMemory(0x58E7A8, Add, 0x00000080);
		SetMemory(0x58E7A4, Add, 0x000000A0);
		SetMemory(0x58E7AC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000A0);
		SetMemory(0x58E7A8, Subtract, 0x000000A0);
		SetMemory(0x58E7A4, Add, 0x00000080);
		SetMemory(0x58E7AC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000080);
		SetMemory(0x58E7A8, Subtract, 0x00000080);
		SetMemory(0x58E7A4, Subtract, 0x000000A0);
		SetMemory(0x58E7AC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000A0);
		SetMemory(0x58E7A8, Add, 0x000000A0);
		SetMemory(0x58E7A4, Subtract, 0x00000080);
		SetMemory(0x58E7AC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000060);
		SetMemory(0x58E7A8, Add, 0x00000060);
		SetMemory(0x58E7A4, Add, 0x000000C0);
		SetMemory(0x58E7AC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000C0);
		SetMemory(0x58E7A8, Subtract, 0x000000C0);
		SetMemory(0x58E7A4, Add, 0x00000060);
		SetMemory(0x58E7AC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000060);
		SetMemory(0x58E7A8, Subtract, 0x00000060);
		SetMemory(0x58E7A4, Subtract, 0x000000C0);
		SetMemory(0x58E7AC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000C0);
		SetMemory(0x58E7A8, Add, 0x000000C0);
		SetMemory(0x58E7A4, Subtract, 0x00000060);
		SetMemory(0x58E7AC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000040);
		SetMemory(0x58E7A8, Add, 0x00000040);
		SetMemory(0x58E7A4, Add, 0x000000E0);
		SetMemory(0x58E7AC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x000000E0);
		SetMemory(0x58E7A8, Subtract, 0x000000E0);
		SetMemory(0x58E7A4, Add, 0x00000040);
		SetMemory(0x58E7AC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000040);
		SetMemory(0x58E7A8, Subtract, 0x00000040);
		SetMemory(0x58E7A4, Subtract, 0x000000E0);
		SetMemory(0x58E7AC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x000000E0);
		SetMemory(0x58E7A8, Add, 0x000000E0);
		SetMemory(0x58E7A4, Subtract, 0x00000040);
		SetMemory(0x58E7AC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000020);
		SetMemory(0x58E7A8, Add, 0x00000020);
		SetMemory(0x58E7A4, Add, 0x00000100);
		SetMemory(0x58E7AC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000100);
		SetMemory(0x58E7A8, Subtract, 0x00000100);
		SetMemory(0x58E7A4, Add, 0x00000020);
		SetMemory(0x58E7AC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Subtract, 0x00000020);
		SetMemory(0x58E7A8, Subtract, 0x00000020);
		SetMemory(0x58E7A4, Subtract, 0x00000100);
		SetMemory(0x58E7AC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E7A0, Add, 0x00000100);
		SetMemory(0x58E7A8, Add, 0x00000100);
		SetMemory(0x58E7A4, Subtract, 0x00000020);
		SetMemory(0x58E7AC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetSwitch("JunkYardDog", Set);
		SetSwitch("ComputerAlliy", Set);
		Wait(3000);
		SetDeaths(AllPlayers, SetTo, 8001, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "130 + 1n Arbiter", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Siege", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(4, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
		Wait(100);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P9);
		GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P10);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P10);
		GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, "60 + 1n Danimoth", P10, "Anywhere", CurrentPlayer);
		GiveUnits(All, "50 + 1n Battlecruiser", P9, "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		Wait(1000);
		GiveUnits(All, "130 + 1n Arbiter", P9, "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", P10, "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		SetSwitch("JunkYardDog", Clear);
		SetSwitch("ComputerAlliy", Clear);
		SetDeaths(AllPlayers, SetTo, 8002, " `SkillText_Uiltimate");
		Wait(2800);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Carrier", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 150, " `UltimateCoolTime");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		SetSwitch("JunkYardDog", Set);
		SetSwitch("ComputerAlliy", Set);
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "40 + 1n Zergling", CurrentPlayer, "Anywhere", P8);
		Wait(0);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P12);
		GiveUnits(All, "100 + 1n Hyperion", P7, "Anywhere", P12);
		GiveUnits(All, "40 + 1n Zergling", P8, "Anywhere", P12);
		Wait(2000);
		GiveUnits(All, "100 + 1n Hyperion", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "40 + 1n Zergling", P12, "Anywhere", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 8100, " `SkillText_Uiltimate");
		SetSwitch("Recall - Anzu", Set);
		GiveUnits(All, "130 + 1n Arbiter", P12, "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Order("40 + 1n Zergling", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(500);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "40 + 1n Zergling", CurrentPlayer, "Anywhere", P8);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		KillUnitAt(3, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(CurrentPlayer, Subtract, 150, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 330, " `SkillStep");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Bring(CurrentPlayer, AtMost, 2, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 149, " `UltimateCoolTime");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
		Bring(CurrentPlayer, AtLeast, 1, "50 + 1n Battlecruiser", "Anywhere");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zergling", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(2, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveUnit(2, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(2, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveUnit(2, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(8, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Zergling", CurrentPlayer, "Anywhere", Attack, "08.Anzu_Bozo");
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

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "08.Anzu_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "130 + 1n Arbiter", "Anywhere");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(4, " * Devouring One", "[Skill]Unit_Wait_5", CurrentPlayer, {
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
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "130 + 1n Arbiter", "Anywhere");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(4, " * Devouring One", "[Skill]Unit_Wait_5", CurrentPlayer, {
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
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		MoveUnit(1, " * Devouring One", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", "130 + 1n Arbiter", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Bring(CurrentPlayer, Exactly, 0, "130 + 1n Arbiter", "Anywhere");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("JunkYardDog", Set);
		SetSwitch("ComputerAlliy", Set);
		SetDeaths(AllPlayers, SetTo, 8101, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, "100 + 1n Hyperion", P7, "Anywhere", CurrentPlayer);
		GiveUnits(All, "40 + 1n Zergling", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "40 + 1n Zergling", P7, "Anywhere", CurrentPlayer);
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 8102, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, SetTo, 9, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, " * Devouring One", "Anywhere", CurrentPlayer);
		GiveUnits(All, " * Devouring One", P12, "Anywhere", CurrentPlayer);
		MoveLocation("08.Anzu", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		GiveUnits(All, "100 + 1n Hyperion", P7, "Anywhere", CurrentPlayer);
		GiveUnits(All, "40 + 1n Zergling", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", CurrentPlayer);
		GiveUnits(All, "40 + 1n Zergling", P7, "Anywhere", CurrentPlayer);
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "08.Anzu");
		Wait(50);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		GiveUnits(1, " * Devouring One", CurrentPlayer, "Anywhere", P12);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, " * Devouring One", "Anywhere", CurrentPlayer);
		GiveUnits(All, " * Devouring One", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "40 + 1n Zergling", CurrentPlayer, "Anywhere", P7);
		Wait(0);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P7);
		GiveUnits(All, "40 + 1n Zergling", P7, "Anywhere", P8);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		CreateUnitWithProperties(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
			clocked = false,
			burrowed = false,
			intransit = false,
			hallucinated = true,
			invincible = false,
			hitpoint = 100,
			shield = 100,
			energy = 100,
			resource = 0,
			hanger = 0,
		});
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		MoveLocation("08.Anzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, " * Devouring One", "Anywhere", CurrentPlayer);
		MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "08.Anzu");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, " * Devouring One", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		SetSwitch("Recall - Anzu", Clear);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillStep");
		SetSwitch("JunkYardDog", Clear);
		SetSwitch("ComputerAlliy", Clear);
		Wait(1000);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}