Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 06.Negev
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Sarah Kerrigan");
	},
	actions = {
		Comment("06.Negev");
		SetDeaths(AllPlayers, SetTo, 6, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 1000, " * Sarah Kerrigan");
		CreateUnit(1, " * Sarah Kerrigan", "[Select]Select Unit", CurrentPlayer);
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

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtMost, 24);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\x13\x17[ O Skill \x04은 25레벨 이상시에만 사용이 가능합니다. \x17]", 0);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 6000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 1800, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 84, " `UniqueSkill");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 100, " `SkillStep");
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 200, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
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
		SetDeaths(AllPlayers, SetTo, 6000, " `SkillText");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 6001, " `SkillText");
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 6100, " `SkillText");
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 550, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Cleared);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 550, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 6000, " `SkillText_Uiltimate");
		KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 550, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Set);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 900, Gas);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveLocation("06.Negev_Unique", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
	},
}

Trigger { -- Skill : Unique
	players = {Force1},
	conditions = {
		Deaths(P1, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P1, AtLeast, 1, " `UniqueSkill");
		Bring(P1, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1},
	conditions = {
		Deaths(P2, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P2, AtLeast, 1, " `UniqueSkill");
		Bring(P2, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1},
	conditions = {
		Deaths(P3, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P3, AtLeast, 1, " `UniqueSkill");
		Bring(P3, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(P4, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P4, AtLeast, 1, " `UniqueSkill");
		Bring(P4, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(P5, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P5, AtLeast, 1, " `UniqueSkill");
		Bring(P5, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(P6, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(P6, AtLeast, 1, " `UniqueSkill");
		Bring(P6, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "06.Negev_Unique");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemShield");
		ModifyUnitShields(All, "Men", CurrentPlayer, "Anywhere", 2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		MoveLocation("06.Negev_Unique", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		ModifyUnitShields(All, "Men", P4, "06.Negev_Unique", 2);
		ModifyUnitShields(All, "Men", P5, "06.Negev_Unique", 2);
		ModifyUnitShields(All, "Men", P6, "06.Negev_Unique", 2);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(130);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(300);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(130);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(300);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(130);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000A4);
		SetMemory(0x58E6B0, Add, 0x000000A4);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x000000A4);
		SetMemory(0x58E6BC, Add, 0x000000A4);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000A4);
		SetMemory(0x58E6B0, Subtract, 0x000000A4);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x000000A4);
		SetMemory(0x58E6BC, Subtract, 0x000000A4);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x000000A4);
		SetMemory(0x58E6BC, Add, 0x000000A4);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000A4);
		SetMemory(0x58E6B0, Subtract, 0x000000A4);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x000000A4);
		SetMemory(0x58E6BC, Subtract, 0x000000A4);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000A4);
		SetMemory(0x58E6B0, Add, 0x000000A4);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(800);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Terran Science Vessel", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		ModifyUnitHitPoints(All, "80 + 1n Marine", CurrentPlayer, "Anywhere", 1);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		ModifyUnitHitPoints(All, "80 + 1n Marine", CurrentPlayer, "Anywhere", 1);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(230);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Add, 0x00000050);
		SetMemory(0x58E6BC, Add, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000050);
		SetMemory(0x58E6B0, Subtract, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000050);
		SetMemory(0x58E6B0, Add, 0x00000050);
		SetMemory(0x58E6B4, Subtract, 0x00000050);
		SetMemory(0x58E6BC, Subtract, 0x00000050);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Add, 0x00000036);
		SetMemory(0x58E6BC, Add, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000036);
		SetMemory(0x58E6B0, Subtract, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000036);
		SetMemory(0x58E6B0, Add, 0x00000036);
		SetMemory(0x58E6B4, Subtract, 0x00000036);
		SetMemory(0x58E6BC, Subtract, 0x00000036);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Terran Science Vessel", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Add, 0x0000001B);
		SetMemory(0x58E6BC, Add, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x0000001B);
		SetMemory(0x58E6B0, Subtract, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000001B);
		SetMemory(0x58E6B0, Add, 0x0000001B);
		SetMemory(0x58E6B4, Subtract, 0x0000001B);
		SetMemory(0x58E6BC, Subtract, 0x0000001B);
		MoveUnit(1, "Terran Science Vessel", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Terran Science Vessel", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(230);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Sarah Kerrigan", CurrentPlayer, "Anywhere", Move, "06.Negev_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000140);
		SetMemory(0x58E6B0, Subtract, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000140);
		SetMemory(0x58E6BC, Subtract, 0x00000140);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 6002, " `SkillText");
		Wait(700);
		KillUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Sarah Kerrigan", CurrentPlayer, "Anywhere", Move, "06.Negev_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF00);
		SetMemory(0x58E6BC, Add, 0xFFFFFF00);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF00);
		SetMemory(0x58E6B0, Add, 0xFFFFFF00);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF80);
		SetMemory(0x58E6BC, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF80);
		SetMemory(0x58E6B0, Add, 0xFFFFFF80);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000062);
		SetMemory(0x58E6B0, Add, 0x00000062);
		SetMemory(0x58E6B4, Add, 0x000000ED);
		SetMemory(0x58E6BC, Add, 0x000000ED);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000ED);
		SetMemory(0x58E6B0, Add, 0x000000ED);
		SetMemory(0x58E6B4, Add, 0xFFFFFF9E);
		SetMemory(0x58E6BC, Add, 0xFFFFFF9E);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B0, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B4, Add, 0xFFFFFF13);
		SetMemory(0x58E6BC, Add, 0xFFFFFF13);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF13);
		SetMemory(0x58E6B0, Add, 0xFFFFFF13);
		SetMemory(0x58E6B4, Add, 0x00000062);
		SetMemory(0x58E6BC, Add, 0x00000062);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000031);
		SetMemory(0x58E6B0, Add, 0x00000031);
		SetMemory(0x58E6B4, Add, 0x00000076);
		SetMemory(0x58E6BC, Add, 0x00000076);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000076);
		SetMemory(0x58E6B0, Add, 0x00000076);
		SetMemory(0x58E6B4, Add, 0xFFFFFFCF);
		SetMemory(0x58E6BC, Add, 0xFFFFFFCF);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B0, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B4, Add, 0xFFFFFF8A);
		SetMemory(0x58E6BC, Add, 0xFFFFFF8A);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B0, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B4, Add, 0x00000031);
		SetMemory(0x58E6BC, Add, 0x00000031);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000B5);
		SetMemory(0x58E6B0, Add, 0x000000B5);
		SetMemory(0x58E6B4, Add, 0x000000B5);
		SetMemory(0x58E6BC, Add, 0x000000B5);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000B5);
		SetMemory(0x58E6B0, Add, 0x000000B5);
		SetMemory(0x58E6B4, Add, 0xFFFFFF4B);
		SetMemory(0x58E6BC, Add, 0xFFFFFF4B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B0, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B4, Add, 0xFFFFFF4B);
		SetMemory(0x58E6BC, Add, 0xFFFFFF4B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B0, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B4, Add, 0x000000B5);
		SetMemory(0x58E6BC, Add, 0x000000B5);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000005B);
		SetMemory(0x58E6B0, Add, 0x0000005B);
		SetMemory(0x58E6B4, Add, 0x0000005B);
		SetMemory(0x58E6BC, Add, 0x0000005B);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000005B);
		SetMemory(0x58E6B0, Add, 0x0000005B);
		SetMemory(0x58E6B4, Add, 0xFFFFFFA5);
		SetMemory(0x58E6BC, Add, 0xFFFFFFA5);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B0, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B4, Add, 0xFFFFFFA5);
		SetMemory(0x58E6BC, Add, 0xFFFFFFA5);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B0, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B4, Add, 0x0000005B);
		SetMemory(0x58E6BC, Add, 0x0000005B);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000ED);
		SetMemory(0x58E6B0, Add, 0x000000ED);
		SetMemory(0x58E6B4, Add, 0x00000062);
		SetMemory(0x58E6BC, Add, 0x00000062);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000062);
		SetMemory(0x58E6B0, Add, 0x00000062);
		SetMemory(0x58E6B4, Add, 0xFFFFFF13);
		SetMemory(0x58E6BC, Add, 0xFFFFFF13);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF13);
		SetMemory(0x58E6B0, Add, 0xFFFFFF13);
		SetMemory(0x58E6B4, Add, 0xFFFFFF9E);
		SetMemory(0x58E6BC, Add, 0xFFFFFF9E);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B0, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B4, Add, 0x000000ED);
		SetMemory(0x58E6BC, Add, 0x000000ED);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000076);
		SetMemory(0x58E6B0, Add, 0x00000076);
		SetMemory(0x58E6B4, Add, 0x00000031);
		SetMemory(0x58E6BC, Add, 0x00000031);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000031);
		SetMemory(0x58E6B0, Add, 0x00000031);
		SetMemory(0x58E6B4, Add, 0xFFFFFF8A);
		SetMemory(0x58E6BC, Add, 0xFFFFFF8A);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B0, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B4, Add, 0xFFFFFFCF);
		SetMemory(0x58E6BC, Add, 0xFFFFFFCF);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B0, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B4, Add, 0x00000076);
		SetMemory(0x58E6BC, Add, 0x00000076);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF00);
		SetMemory(0x58E6BC, Add, 0xFFFFFF00);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF00);
		SetMemory(0x58E6B0, Add, 0xFFFFFF00);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF80);
		SetMemory(0x58E6BC, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF80);
		SetMemory(0x58E6B0, Add, 0xFFFFFF80);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000ED);
		SetMemory(0x58E6B0, Add, 0x000000ED);
		SetMemory(0x58E6B4, Add, 0xFFFFFF9E);
		SetMemory(0x58E6BC, Add, 0xFFFFFF9E);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B0, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B4, Add, 0xFFFFFF13);
		SetMemory(0x58E6BC, Add, 0xFFFFFF13);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF13);
		SetMemory(0x58E6B0, Add, 0xFFFFFF13);
		SetMemory(0x58E6B4, Add, 0x00000062);
		SetMemory(0x58E6BC, Add, 0x00000062);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000062);
		SetMemory(0x58E6B0, Add, 0x00000062);
		SetMemory(0x58E6B4, Add, 0x000000ED);
		SetMemory(0x58E6BC, Add, 0x000000ED);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000076);
		SetMemory(0x58E6B0, Add, 0x00000076);
		SetMemory(0x58E6B4, Add, 0xFFFFFFCF);
		SetMemory(0x58E6BC, Add, 0xFFFFFFCF);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B0, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B4, Add, 0xFFFFFF8A);
		SetMemory(0x58E6BC, Add, 0xFFFFFF8A);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B0, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B4, Add, 0x00000031);
		SetMemory(0x58E6BC, Add, 0x00000031);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000031);
		SetMemory(0x58E6B0, Add, 0x00000031);
		SetMemory(0x58E6B4, Add, 0x00000076);
		SetMemory(0x58E6BC, Add, 0x00000076);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000B5);
		SetMemory(0x58E6B0, Add, 0x000000B5);
		SetMemory(0x58E6B4, Add, 0xFFFFFF4B);
		SetMemory(0x58E6BC, Add, 0xFFFFFF4B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B0, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B4, Add, 0xFFFFFF4B);
		SetMemory(0x58E6BC, Add, 0xFFFFFF4B);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B0, Add, 0xFFFFFF4B);
		SetMemory(0x58E6B4, Add, 0x000000B5);
		SetMemory(0x58E6BC, Add, 0x000000B5);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000B5);
		SetMemory(0x58E6B0, Add, 0x000000B5);
		SetMemory(0x58E6B4, Add, 0x000000B5);
		SetMemory(0x58E6BC, Add, 0x000000B5);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000005B);
		SetMemory(0x58E6B0, Add, 0x0000005B);
		SetMemory(0x58E6B4, Add, 0xFFFFFFA5);
		SetMemory(0x58E6BC, Add, 0xFFFFFFA5);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B0, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B4, Add, 0xFFFFFFA5);
		SetMemory(0x58E6BC, Add, 0xFFFFFFA5);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B0, Add, 0xFFFFFFA5);
		SetMemory(0x58E6B4, Add, 0x0000005B);
		SetMemory(0x58E6BC, Add, 0x0000005B);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x0000005B);
		SetMemory(0x58E6B0, Add, 0x0000005B);
		SetMemory(0x58E6B4, Add, 0x0000005B);
		SetMemory(0x58E6BC, Add, 0x0000005B);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000062);
		SetMemory(0x58E6B0, Add, 0x00000062);
		SetMemory(0x58E6B4, Add, 0xFFFFFF13);
		SetMemory(0x58E6BC, Add, 0xFFFFFF13);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF13);
		SetMemory(0x58E6B0, Add, 0xFFFFFF13);
		SetMemory(0x58E6B4, Add, 0xFFFFFF9E);
		SetMemory(0x58E6BC, Add, 0xFFFFFF9E);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B0, Add, 0xFFFFFF9E);
		SetMemory(0x58E6B4, Add, 0x000000ED);
		SetMemory(0x58E6BC, Add, 0x000000ED);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000ED);
		SetMemory(0x58E6B0, Add, 0x000000ED);
		SetMemory(0x58E6B4, Add, 0x00000062);
		SetMemory(0x58E6BC, Add, 0x00000062);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000031);
		SetMemory(0x58E6B0, Add, 0x00000031);
		SetMemory(0x58E6B4, Add, 0xFFFFFF8A);
		SetMemory(0x58E6BC, Add, 0xFFFFFF8A);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B0, Add, 0xFFFFFF8A);
		SetMemory(0x58E6B4, Add, 0xFFFFFFCF);
		SetMemory(0x58E6BC, Add, 0xFFFFFFCF);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B0, Add, 0xFFFFFFCF);
		SetMemory(0x58E6B4, Add, 0x00000076);
		SetMemory(0x58E6BC, Add, 0x00000076);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000076);
		SetMemory(0x58E6B0, Add, 0x00000076);
		SetMemory(0x58E6B4, Add, 0x00000031);
		SetMemory(0x58E6BC, Add, 0x00000031);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF00);
		SetMemory(0x58E6BC, Add, 0xFFFFFF00);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF00);
		SetMemory(0x58E6B0, Add, 0xFFFFFF00);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0xFFFFFF80);
		SetMemory(0x58E6BC, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0xFFFFFF80);
		SetMemory(0x58E6B0, Add, 0xFFFFFF80);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000A0);
		SetMemory(0x58E6B0, Add, 0x000000A0);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x000000A0);
		SetMemory(0x58E6BC, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000A0);
		SetMemory(0x58E6B0, Subtract, 0x000000A0);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x000000A0);
		SetMemory(0x58E6BC, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000140);
		SetMemory(0x58E6B0, Subtract, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000140);
		SetMemory(0x58E6BC, Subtract, 0x00000140);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000E0);
		SetMemory(0x58E6B0, Add, 0x000000E0);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x000000E0);
		SetMemory(0x58E6BC, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000E0);
		SetMemory(0x58E6B0, Subtract, 0x000000E0);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x000000E0);
		SetMemory(0x58E6BC, Subtract, 0x000000E0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000060);
		SetMemory(0x58E6B0, Add, 0x00000060);
		SetMemory(0x58E6B4, Add, 0x00000000);
		SetMemory(0x58E6BC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000000);
		SetMemory(0x58E6B0, Subtract, 0x00000000);
		SetMemory(0x58E6B4, Add, 0x00000060);
		SetMemory(0x58E6BC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000060);
		SetMemory(0x58E6B0, Subtract, 0x00000060);
		SetMemory(0x58E6B4, Subtract, 0x00000000);
		SetMemory(0x58E6BC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000000);
		SetMemory(0x58E6B0, Add, 0x00000000);
		SetMemory(0x58E6B4, Subtract, 0x00000060);
		SetMemory(0x58E6BC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000E0);
		SetMemory(0x58E6B0, Add, 0x000000E0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000E0);
		SetMemory(0x58E6BC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000E0);
		SetMemory(0x58E6B0, Subtract, 0x000000E0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000E0);
		SetMemory(0x58E6BC, Subtract, 0x000000E0);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000E0);
		SetMemory(0x58E6B0, Add, 0x000000E0);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x000000E0);
		SetMemory(0x58E6BC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000E0);
		SetMemory(0x58E6B0, Subtract, 0x000000E0);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Subtract, 0x000000E0);
		SetMemory(0x58E6BC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000020);
		SetMemory(0x58E6B0, Add, 0x00000020);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000020);
		SetMemory(0x58E6BC, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000020);
		SetMemory(0x58E6B0, Subtract, 0x00000020);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Subtract, 0x00000020);
		SetMemory(0x58E6BC, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 32, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		Wait(1500);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		MoveLocation("06.Negev_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("Recall - Negev", Set);
		Wait(5750);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000140);
		SetMemory(0x58E6BC, Subtract, 0x00000140);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "80 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "80 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000140);
		SetMemory(0x58E6B0, Subtract, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000140);
		SetMemory(0x58E6BC, Subtract, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000140);
		SetMemory(0x58E6B0, Subtract, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000100);
		SetMemory(0x58E6BC, Subtract, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000100);
		SetMemory(0x58E6BC, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000100);
		SetMemory(0x58E6B0, Add, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000100);
		SetMemory(0x58E6B0, Subtract, 0x00000100);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x000000C0);
		SetMemory(0x58E6BC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x000000C0);
		SetMemory(0x58E6BC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x000000C0);
		SetMemory(0x58E6B0, Add, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x000000C0);
		SetMemory(0x58E6B0, Subtract, 0x000000C0);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000080);
		SetMemory(0x58E6BC, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000080);
		SetMemory(0x58E6B0, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000080);
		SetMemory(0x58E6B0, Add, 0x00000080);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		SetMemory(0x58E6B4, Add, 0x00000040);
		SetMemory(0x58E6BC, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000040);
		SetMemory(0x58E6B0, Add, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "130 + 1n Norad", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B8, Add, 0x00000140);
		SetMemory(0x58E6B0, Add, 0x00000140);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B8, Subtract, 0x00000040);
		SetMemory(0x58E6B0, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(5, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "130 + 1n Norad", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		SetMemory(0x58E6B4, Add, 0x00000140);
		SetMemory(0x58E6BC, Add, 0x00000140);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000080);
		SetMemory(0x58E6BC, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		SetMemory(0x58E6B4, Subtract, 0x00000040);
		SetMemory(0x58E6BC, Subtract, 0x00000040);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		MoveLocation("06.Negev", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "06.Negev");
		Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "06.Negev");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		Wait(2000);
		KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(500);
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		SetSwitch("Recall - Negev", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}