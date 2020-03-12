Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 02.Chtholly
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1002, " * Fenix");
	},
	actions = {
		Comment("02.Chtholly");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(AllPlayers, SetTo, 2, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " * Fenix");
		CreateUnit(1, " * Fenix", "[Select]Select Unit", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtMost, 24);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
		DisplayText("\x13\x17[ O Skill \x04은 25레벨 이상시에만 사용이 가능합니다. \x17]", 0);
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("Unique - Chtholly", Set);
	},
	actions = {
		Comment("Skill : Use Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\r\n\x13\x17O Skill \x04패시브를 \x06OFF \x04시킵니다.\r\n", 0);
		SetSwitch("Unique - Chtholly", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("Unique - Chtholly", Cleared);
	},
	actions = {
		Comment("Skill : Use Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\r\n\x13\x17O Skill \x04패시브를 \x06ON \x04시킵니다.\r\n", 0);
		SetSwitch("Unique - Chtholly", Set);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
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

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 110, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2100, " `SkillText");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2000, " `SkillText");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 220, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2002, " `SkillText");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(AllPlayers, SetTo, 2004, " `SkillText");
		SetDeaths(CurrentPlayer, SetTo, 230, " `SkillStep");
		KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 235, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 700, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("UiltimateSwitch", Cleared);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 700, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 240, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2008, " `SkillText_Uiltimate");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("Recall - Chtholly", Set);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 235, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 700, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("UiltimateSwitch", Set);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 40, Gas);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 650, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
		Switch("UiltimateSwitch", Cleared);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 650, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 240, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 2008, " `SkillText_Uiltimate");
		KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("Recall - Chtholly", Set);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 650, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
		Switch("UiltimateSwitch", Set);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 900, Gas);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
	},
	actions = {
		Comment("Skill : Use Unique");
		MoveLocation("[Unique]Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
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
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Score(CurrentPlayer, Custom, AtMost, 24);
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
		SetDeaths(CurrentPlayer, SetTo, 0, " `UniqueSkill");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Deaths(CurrentPlayer, AtMost, 200, " `SkillStep");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Deaths(CurrentPlayer, AtLeast, 300, " `SkillStep");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Switch("Unique - Chtholly", Set);
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, " * Fenix", "[Unique]Chtholly", CurrentPlayer);
		SetInvincibility(Enable, " * Fenix", CurrentPlayer, "Anywhere");
		ModifyUnitHitPoints(All, " * Fenix", CurrentPlayer, "Anywhere", 1);
		SetDeaths(CurrentPlayer, SetTo, 1000, " * Fenix");
		SetDeaths(CurrentPlayer, SetTo, 60, " `UniqueSkill");
		SetDeaths(AllPlayers, SetTo, 2999, " `SkillText");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueCoolTime");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Fenix");
		Switch("Unique - Chtholly", Cleared);
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, AtLeast, 2, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("02.Chtholly_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		KillUnitAt(All, " * Fenix", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 1002, " * Fenix");
		SetDeaths(CurrentPlayer, SetTo, 0, " `UniqueSkill");
		SetDeaths(CurrentPlayer, SetTo, 2880, " `UniqueCoolTime");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(100);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000030);
		SetMemory(0x58E570, Add, 0x00000030);
		SetMemory(0x58E574, Add, 0x00000030);
		SetMemory(0x58E57C, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000030);
		SetMemory(0x58E570, Subtract, 0x00000030);
		SetMemory(0x58E574, Add, 0x00000030);
		SetMemory(0x58E57C, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000030);
		SetMemory(0x58E570, Subtract, 0x00000030);
		SetMemory(0x58E574, Subtract, 0x00000030);
		SetMemory(0x58E57C, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000030);
		SetMemory(0x58E570, Add, 0x00000030);
		SetMemory(0x58E574, Subtract, 0x00000030);
		SetMemory(0x58E57C, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(50);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000070);
		SetMemory(0x58E570, Subtract, 0x00000070);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000070);
		SetMemory(0x58E57C, Subtract, 0x00000070);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(220);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000005A);
		SetMemory(0x58E570, Add, 0x0000005A);
		SetMemory(0x58E574, Add, 0x0000005A);
		SetMemory(0x58E57C, Add, 0x0000005A);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000005A);
		SetMemory(0x58E570, Subtract, 0x0000005A);
		SetMemory(0x58E574, Add, 0x0000005A);
		SetMemory(0x58E57C, Add, 0x0000005A);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000005A);
		SetMemory(0x58E570, Subtract, 0x0000005A);
		SetMemory(0x58E574, Subtract, 0x0000005A);
		SetMemory(0x58E57C, Subtract, 0x0000005A);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000005A);
		SetMemory(0x58E570, Add, 0x0000005A);
		SetMemory(0x58E574, Subtract, 0x0000005A);
		SetMemory(0x58E57C, Subtract, 0x0000005A);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(740);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "40 + 1n Marine", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000010);
		SetMemory(0x58E570, Add, 0x00000010);
		SetMemory(0x58E574, Add, 0x00000010);
		SetMemory(0x58E57C, Add, 0x00000010);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000010);
		SetMemory(0x58E570, Subtract, 0x00000010);
		SetMemory(0x58E574, Add, 0x00000010);
		SetMemory(0x58E57C, Add, 0x00000010);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000010);
		SetMemory(0x58E570, Subtract, 0x00000010);
		SetMemory(0x58E574, Subtract, 0x00000010);
		SetMemory(0x58E57C, Subtract, 0x00000010);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000010);
		SetMemory(0x58E570, Add, 0x00000010);
		SetMemory(0x58E574, Subtract, 0x00000010);
		SetMemory(0x58E57C, Subtract, 0x00000010);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000030);
		SetMemory(0x58E570, Add, 0x00000030);
		SetMemory(0x58E574, Add, 0x00000030);
		SetMemory(0x58E57C, Add, 0x00000030);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000030);
		SetMemory(0x58E570, Subtract, 0x00000030);
		SetMemory(0x58E574, Add, 0x00000030);
		SetMemory(0x58E57C, Add, 0x00000030);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000030);
		SetMemory(0x58E570, Subtract, 0x00000030);
		SetMemory(0x58E574, Subtract, 0x00000030);
		SetMemory(0x58E57C, Subtract, 0x00000030);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000030);
		SetMemory(0x58E570, Add, 0x00000030);
		SetMemory(0x58E574, Subtract, 0x00000030);
		SetMemory(0x58E57C, Subtract, 0x00000030);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000070);
		SetMemory(0x58E570, Subtract, 0x00000070);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000070);
		SetMemory(0x58E570, Subtract, 0x00000070);
		SetMemory(0x58E574, Subtract, 0x00000070);
		SetMemory(0x58E57C, Subtract, 0x00000070);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Subtract, 0x00000070);
		SetMemory(0x58E57C, Subtract, 0x00000070);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000014);
		SetMemory(0x58E570, Add, 0x00000014);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000014);
		SetMemory(0x58E57C, Add, 0x00000014);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000014);
		SetMemory(0x58E570, Subtract, 0x00000014);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000014);
		SetMemory(0x58E57C, Subtract, 0x00000014);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000028);
		SetMemory(0x58E570, Add, 0x00000028);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000028);
		SetMemory(0x58E57C, Add, 0x00000028);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000028);
		SetMemory(0x58E570, Subtract, 0x00000028);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000028);
		SetMemory(0x58E57C, Subtract, 0x00000028);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000003C);
		SetMemory(0x58E570, Add, 0x0000003C);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000003C);
		SetMemory(0x58E57C, Add, 0x0000003C);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000003C);
		SetMemory(0x58E570, Subtract, 0x0000003C);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000003C);
		SetMemory(0x58E57C, Subtract, 0x0000003C);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000050);
		SetMemory(0x58E570, Subtract, 0x00000050);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000050);
		SetMemory(0x58E57C, Subtract, 0x00000050);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000064);
		SetMemory(0x58E570, Add, 0x00000064);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000064);
		SetMemory(0x58E57C, Add, 0x00000064);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000064);
		SetMemory(0x58E570, Subtract, 0x00000064);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000064);
		SetMemory(0x58E57C, Subtract, 0x00000064);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000078);
		SetMemory(0x58E570, Add, 0x00000078);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000078);
		SetMemory(0x58E57C, Add, 0x00000078);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000078);
		SetMemory(0x58E570, Subtract, 0x00000078);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000078);
		SetMemory(0x58E57C, Subtract, 0x00000078);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000008C);
		SetMemory(0x58E570, Add, 0x0000008C);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000008C);
		SetMemory(0x58E57C, Add, 0x0000008C);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000008C);
		SetMemory(0x58E570, Subtract, 0x0000008C);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000008C);
		SetMemory(0x58E57C, Subtract, 0x0000008C);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000A0);
		SetMemory(0x58E570, Subtract, 0x000000A0);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000A0);
		SetMemory(0x58E57C, Subtract, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000B5);
		SetMemory(0x58E570, Subtract, 0x000000B5);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000B5);
		SetMemory(0x58E57C, Subtract, 0x000000B5);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Lurker", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000005A);
		SetMemory(0x58E570, Add, 0x0000005A);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000005A);
		SetMemory(0x58E57C, Add, 0x0000005A);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000005A);
		SetMemory(0x58E570, Subtract, 0x0000005A);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000005A);
		SetMemory(0x58E57C, Subtract, 0x0000005A);
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(3500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000002D);
		SetMemory(0x58E570, Add, 0x0000002D);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000002D);
		SetMemory(0x58E57C, Add, 0x0000002D);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000002D);
		SetMemory(0x58E570, Subtract, 0x0000002D);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000002D);
		SetMemory(0x58E57C, Subtract, 0x0000002D);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000005A);
		SetMemory(0x58E570, Add, 0x0000005A);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000005A);
		SetMemory(0x58E57C, Add, 0x0000005A);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000005A);
		SetMemory(0x58E570, Subtract, 0x0000005A);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000005A);
		SetMemory(0x58E57C, Subtract, 0x0000005A);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000087);
		SetMemory(0x58E570, Add, 0x00000087);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000087);
		SetMemory(0x58E57C, Add, 0x00000087);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000087);
		SetMemory(0x58E570, Subtract, 0x00000087);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000087);
		SetMemory(0x58E57C, Subtract, 0x00000087);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000B5);
		SetMemory(0x58E570, Subtract, 0x000000B5);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000B5);
		SetMemory(0x58E57C, Subtract, 0x000000B5);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 2001, " `SkillText");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x0000005A);
		SetMemory(0x58E570, Add, 0x0000005A);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x0000005A);
		SetMemory(0x58E57C, Add, 0x0000005A);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x0000005A);
		SetMemory(0x58E570, Subtract, 0x0000005A);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x0000005A);
		SetMemory(0x58E57C, Subtract, 0x0000005A);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Torrasque (Ultralisk)", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "Torrasque (Ultralisk)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Torrasque (Ultralisk)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000B5);
		SetMemory(0x58E570, Subtract, 0x000000B5);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000B5);
		SetMemory(0x58E57C, Subtract, 0x000000B5);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(2750);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000B5);
		SetMemory(0x58E570, Subtract, 0x000000B5);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000B5);
		SetMemory(0x58E57C, Subtract, 0x000000B5);
		MoveUnit(8, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillCount");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(650);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		KillUnitAt(All, "60 + 1n Siege", "02.Chtholly_Bozo", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000A0);
		SetMemory(0x58E570, Subtract, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000A0);
		SetMemory(0x58E570, Subtract, 0x000000A0);
		SetMemory(0x58E574, Subtract, 0x000000A0);
		SetMemory(0x58E57C, Subtract, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Subtract, 0x000000A0);
		SetMemory(0x58E57C, Subtract, 0x000000A0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000E0);
		SetMemory(0x58E570, Add, 0x000000E0);
		SetMemory(0x58E574, Add, 0x000000E0);
		SetMemory(0x58E57C, Add, 0x000000E0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000E0);
		SetMemory(0x58E570, Subtract, 0x000000E0);
		SetMemory(0x58E574, Add, 0x000000E0);
		SetMemory(0x58E57C, Add, 0x000000E0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000E0);
		SetMemory(0x58E570, Subtract, 0x000000E0);
		SetMemory(0x58E574, Subtract, 0x000000E0);
		SetMemory(0x58E57C, Subtract, 0x000000E0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000E0);
		SetMemory(0x58E570, Add, 0x000000E0);
		SetMemory(0x58E574, Subtract, 0x000000E0);
		SetMemory(0x58E57C, Subtract, 0x000000E0);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000100);
		SetMemory(0x58E570, Subtract, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000100);
		SetMemory(0x58E570, Subtract, 0x00000100);
		SetMemory(0x58E574, Subtract, 0x00000100);
		SetMemory(0x58E57C, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Subtract, 0x00000100);
		SetMemory(0x58E57C, Subtract, 0x00000100);
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Unclean One (Defiler)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000E0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000E0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000E0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF20);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF20);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF20);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF20);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000001D);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x0000001D);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFFE3);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFFE3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFE3);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFFE3);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x0000001D);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x0000001D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000003A);
		SetMemory(0x58E574, Add, 0x000000D8);
		SetMemory(0x58E578, Add, 0x0000003A);
		SetMemory(0x58E57C, Add, 0x000000D8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000D8);
		SetMemory(0x58E574, Add, 0xFFFFFFC6);
		SetMemory(0x58E578, Add, 0x000000D8);
		SetMemory(0x58E57C, Add, 0xFFFFFFC6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC6);
		SetMemory(0x58E574, Add, 0xFFFFFF28);
		SetMemory(0x58E578, Add, 0xFFFFFFC6);
		SetMemory(0x58E57C, Add, 0xFFFFFF28);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF28);
		SetMemory(0x58E574, Add, 0x0000003A);
		SetMemory(0x58E578, Add, 0xFFFFFF28);
		SetMemory(0x58E57C, Add, 0x0000003A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000056);
		SetMemory(0x58E574, Add, 0x000000CF);
		SetMemory(0x58E578, Add, 0x00000056);
		SetMemory(0x58E57C, Add, 0x000000CF);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000CF);
		SetMemory(0x58E574, Add, 0xFFFFFFAA);
		SetMemory(0x58E578, Add, 0x000000CF);
		SetMemory(0x58E57C, Add, 0xFFFFFFAA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFAA);
		SetMemory(0x58E574, Add, 0xFFFFFF31);
		SetMemory(0x58E578, Add, 0xFFFFFFAA);
		SetMemory(0x58E57C, Add, 0xFFFFFF31);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF31);
		SetMemory(0x58E574, Add, 0x00000056);
		SetMemory(0x58E578, Add, 0xFFFFFF31);
		SetMemory(0x58E57C, Add, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0x000000C2);
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0x000000C2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C2);
		SetMemory(0x58E574, Add, 0xFFFFFF90);
		SetMemory(0x58E578, Add, 0x000000C2);
		SetMemory(0x58E57C, Add, 0xFFFFFF90);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF90);
		SetMemory(0x58E574, Add, 0xFFFFFF3E);
		SetMemory(0x58E578, Add, 0xFFFFFF90);
		SetMemory(0x58E57C, Add, 0xFFFFFF3E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF3E);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E578, Add, 0xFFFFFF3E);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0x000000B2);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0x000000B2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B2);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0x000000B2);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0xFFFFFF4E);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0xFFFFFF4E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4E);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0xFFFFFF4E);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000009E);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000009E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFF62);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFF62);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFF62);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFF62);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000009E);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000009E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B2);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0x000000B2);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0xFFFFFF4E);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0xFFFFFF4E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4E);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0xFFFFFF4E);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0x000000B2);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0x000000B2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C2);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E578, Add, 0x000000C2);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0xFFFFFF3E);
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0xFFFFFF3E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF3E);
		SetMemory(0x58E574, Add, 0xFFFFFF90);
		SetMemory(0x58E578, Add, 0xFFFFFF3E);
		SetMemory(0x58E57C, Add, 0xFFFFFF90);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF90);
		SetMemory(0x58E574, Add, 0x000000C2);
		SetMemory(0x58E578, Add, 0xFFFFFF90);
		SetMemory(0x58E57C, Add, 0x000000C2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000CF);
		SetMemory(0x58E574, Add, 0x00000056);
		SetMemory(0x58E578, Add, 0x000000CF);
		SetMemory(0x58E57C, Add, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000056);
		SetMemory(0x58E574, Add, 0xFFFFFF31);
		SetMemory(0x58E578, Add, 0x00000056);
		SetMemory(0x58E57C, Add, 0xFFFFFF31);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF31);
		SetMemory(0x58E574, Add, 0xFFFFFFAA);
		SetMemory(0x58E578, Add, 0xFFFFFF31);
		SetMemory(0x58E57C, Add, 0xFFFFFFAA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFAA);
		SetMemory(0x58E574, Add, 0x000000CF);
		SetMemory(0x58E578, Add, 0xFFFFFFAA);
		SetMemory(0x58E57C, Add, 0x000000CF);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000D8);
		SetMemory(0x58E574, Add, 0x0000003A);
		SetMemory(0x58E578, Add, 0x000000D8);
		SetMemory(0x58E57C, Add, 0x0000003A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000003A);
		SetMemory(0x58E574, Add, 0xFFFFFF28);
		SetMemory(0x58E578, Add, 0x0000003A);
		SetMemory(0x58E57C, Add, 0xFFFFFF28);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF28);
		SetMemory(0x58E574, Add, 0xFFFFFFC6);
		SetMemory(0x58E578, Add, 0xFFFFFF28);
		SetMemory(0x58E57C, Add, 0xFFFFFFC6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC6);
		SetMemory(0x58E574, Add, 0x000000D8);
		SetMemory(0x58E578, Add, 0xFFFFFFC6);
		SetMemory(0x58E57C, Add, 0x000000D8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x0000001D);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x0000001D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000001D);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x0000001D);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFFE3);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFFE3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFE3);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFFE3);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000E0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF20);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF20);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF20);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF20);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000E0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000E0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFFE3);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFFE3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFE3);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFFE3);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x0000001D);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x0000001D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000001D);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x0000001D);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000D8);
		SetMemory(0x58E574, Add, 0xFFFFFFC6);
		SetMemory(0x58E578, Add, 0x000000D8);
		SetMemory(0x58E57C, Add, 0xFFFFFFC6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC6);
		SetMemory(0x58E574, Add, 0xFFFFFF28);
		SetMemory(0x58E578, Add, 0xFFFFFFC6);
		SetMemory(0x58E57C, Add, 0xFFFFFF28);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF28);
		SetMemory(0x58E574, Add, 0x0000003A);
		SetMemory(0x58E578, Add, 0xFFFFFF28);
		SetMemory(0x58E57C, Add, 0x0000003A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000003A);
		SetMemory(0x58E574, Add, 0x000000D8);
		SetMemory(0x58E578, Add, 0x0000003A);
		SetMemory(0x58E57C, Add, 0x000000D8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000CF);
		SetMemory(0x58E574, Add, 0xFFFFFFAA);
		SetMemory(0x58E578, Add, 0x000000CF);
		SetMemory(0x58E57C, Add, 0xFFFFFFAA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFAA);
		SetMemory(0x58E574, Add, 0xFFFFFF31);
		SetMemory(0x58E578, Add, 0xFFFFFFAA);
		SetMemory(0x58E57C, Add, 0xFFFFFF31);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF31);
		SetMemory(0x58E574, Add, 0x00000056);
		SetMemory(0x58E578, Add, 0xFFFFFF31);
		SetMemory(0x58E57C, Add, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000056);
		SetMemory(0x58E574, Add, 0x000000CF);
		SetMemory(0x58E578, Add, 0x00000056);
		SetMemory(0x58E57C, Add, 0x000000CF);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C2);
		SetMemory(0x58E574, Add, 0xFFFFFF90);
		SetMemory(0x58E578, Add, 0x000000C2);
		SetMemory(0x58E57C, Add, 0xFFFFFF90);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF90);
		SetMemory(0x58E574, Add, 0xFFFFFF3E);
		SetMemory(0x58E578, Add, 0xFFFFFF90);
		SetMemory(0x58E57C, Add, 0xFFFFFF3E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF3E);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E578, Add, 0xFFFFFF3E);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0x000000C2);
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0x000000C2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B2);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0x000000B2);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0xFFFFFF4E);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0xFFFFFF4E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4E);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0xFFFFFF4E);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0x000000B2);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0x000000B2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFF62);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFF62);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFF62);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFF62);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000009E);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000009E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000009E);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000009E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0xFFFFFF4E);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0xFFFFFF4E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4E);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0xFFFFFF4E);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0x000000B2);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0x000000B2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B2);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0x000000B2);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000070);
		SetMemory(0x58E574, Add, 0xFFFFFF3E);
		SetMemory(0x58E578, Add, 0x00000070);
		SetMemory(0x58E57C, Add, 0xFFFFFF3E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF3E);
		SetMemory(0x58E574, Add, 0xFFFFFF90);
		SetMemory(0x58E578, Add, 0xFFFFFF3E);
		SetMemory(0x58E57C, Add, 0xFFFFFF90);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF90);
		SetMemory(0x58E574, Add, 0x000000C2);
		SetMemory(0x58E578, Add, 0xFFFFFF90);
		SetMemory(0x58E57C, Add, 0x000000C2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C2);
		SetMemory(0x58E574, Add, 0x00000070);
		SetMemory(0x58E578, Add, 0x000000C2);
		SetMemory(0x58E57C, Add, 0x00000070);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000056);
		SetMemory(0x58E574, Add, 0xFFFFFF31);
		SetMemory(0x58E578, Add, 0x00000056);
		SetMemory(0x58E57C, Add, 0xFFFFFF31);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF31);
		SetMemory(0x58E574, Add, 0xFFFFFFAA);
		SetMemory(0x58E578, Add, 0xFFFFFF31);
		SetMemory(0x58E57C, Add, 0xFFFFFFAA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFAA);
		SetMemory(0x58E574, Add, 0x000000CF);
		SetMemory(0x58E578, Add, 0xFFFFFFAA);
		SetMemory(0x58E57C, Add, 0x000000CF);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000CF);
		SetMemory(0x58E574, Add, 0x00000056);
		SetMemory(0x58E578, Add, 0x000000CF);
		SetMemory(0x58E57C, Add, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000003A);
		SetMemory(0x58E574, Add, 0xFFFFFF28);
		SetMemory(0x58E578, Add, 0x0000003A);
		SetMemory(0x58E57C, Add, 0xFFFFFF28);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF28);
		SetMemory(0x58E574, Add, 0xFFFFFFC6);
		SetMemory(0x58E578, Add, 0xFFFFFF28);
		SetMemory(0x58E57C, Add, 0xFFFFFFC6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC6);
		SetMemory(0x58E574, Add, 0x000000D8);
		SetMemory(0x58E578, Add, 0xFFFFFFC6);
		SetMemory(0x58E57C, Add, 0x000000D8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000D8);
		SetMemory(0x58E574, Add, 0x0000003A);
		SetMemory(0x58E578, Add, 0x000000D8);
		SetMemory(0x58E57C, Add, 0x0000003A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000001D);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x0000001D);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFFE3);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFFE3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFE3);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFFE3);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x0000001D);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x0000001D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF40);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF40);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B1);
		SetMemory(0x58E574, Add, 0xFFFFFFB7);
		SetMemory(0x58E578, Add, 0x000000B1);
		SetMemory(0x58E57C, Add, 0xFFFFFFB7);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4F);
		SetMemory(0x58E574, Add, 0x00000049);
		SetMemory(0x58E578, Add, 0xFFFFFF4F);
		SetMemory(0x58E57C, Add, 0x00000049);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000049);
		SetMemory(0x58E574, Add, 0xFFFFFF4F);
		SetMemory(0x58E578, Add, 0x00000049);
		SetMemory(0x58E57C, Add, 0xFFFFFF4F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB7);
		SetMemory(0x58E574, Add, 0x000000B1);
		SetMemory(0x58E578, Add, 0xFFFFFFB7);
		SetMemory(0x58E57C, Add, 0x000000B1);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF40);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF40);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB7);
		SetMemory(0x58E574, Add, 0xFFFFFF4F);
		SetMemory(0x58E578, Add, 0xFFFFFFB7);
		SetMemory(0x58E57C, Add, 0xFFFFFF4F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000049);
		SetMemory(0x58E574, Add, 0x000000B1);
		SetMemory(0x58E578, Add, 0x00000049);
		SetMemory(0x58E57C, Add, 0x000000B1);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF78);
		SetMemory(0x58E574, Add, 0xFFFFFF78);
		SetMemory(0x58E578, Add, 0xFFFFFF78);
		SetMemory(0x58E57C, Add, 0xFFFFFF78);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000088);
		SetMemory(0x58E574, Add, 0x00000088);
		SetMemory(0x58E578, Add, 0x00000088);
		SetMemory(0x58E57C, Add, 0x00000088);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4F);
		SetMemory(0x58E574, Add, 0xFFFFFFB7);
		SetMemory(0x58E578, Add, 0xFFFFFF4F);
		SetMemory(0x58E57C, Add, 0xFFFFFFB7);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B1);
		SetMemory(0x58E574, Add, 0x00000049);
		SetMemory(0x58E578, Add, 0x000000B1);
		SetMemory(0x58E57C, Add, 0x00000049);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF40);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF40);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(AllPlayers, SetTo, 2003, " `SkillText");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF62);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0xFFFFFF62);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF99);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0xFFFFFF99);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0x0000001C);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0x0000001C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0xFFFFFF85);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0xFFFFFF85);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC9);
		SetMemory(0x58E574, Add, 0x00000096);
		SetMemory(0x58E578, Add, 0xFFFFFFC9);
		SetMemory(0x58E57C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000067);
		SetMemory(0x58E574, Add, 0x0000007B);
		SetMemory(0x58E578, Add, 0x00000067);
		SetMemory(0x58E57C, Add, 0x0000007B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009E);
		SetMemory(0x58E574, Add, 0xFFFFFFE4);
		SetMemory(0x58E578, Add, 0x0000009E);
		SetMemory(0x58E57C, Add, 0xFFFFFFE4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000037);
		SetMemory(0x58E574, Add, 0xFFFFFF6A);
		SetMemory(0x58E578, Add, 0x00000037);
		SetMemory(0x58E57C, Add, 0xFFFFFF6A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000021);
		SetMemory(0x58E574, Add, 0x0000007C);
		SetMemory(0x58E578, Add, 0x00000021);
		SetMemory(0x58E57C, Add, 0x0000007C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000005B);
		SetMemory(0x58E574, Add, 0x0000005B);
		SetMemory(0x58E578, Add, 0x0000005B);
		SetMemory(0x58E57C, Add, 0x0000005B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000007C);
		SetMemory(0x58E574, Add, 0x00000021);
		SetMemory(0x58E578, Add, 0x0000007C);
		SetMemory(0x58E57C, Add, 0x00000021);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000007C);
		SetMemory(0x58E574, Add, 0xFFFFFFDF);
		SetMemory(0x58E578, Add, 0x0000007C);
		SetMemory(0x58E57C, Add, 0xFFFFFFDF);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000005B);
		SetMemory(0x58E574, Add, 0xFFFFFFA5);
		SetMemory(0x58E578, Add, 0x0000005B);
		SetMemory(0x58E57C, Add, 0xFFFFFFA5);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC0);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFFC0);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000021);
		SetMemory(0x58E574, Add, 0xFFFFFF84);
		SetMemory(0x58E578, Add, 0x00000021);
		SetMemory(0x58E57C, Add, 0xFFFFFF84);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFFC0);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFFA0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFFA0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFA0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFFA0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000019);
		SetMemory(0x58E574, Add, 0x0000005D);
		SetMemory(0x58E578, Add, 0x00000019);
		SetMemory(0x58E57C, Add, 0x0000005D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000030);
		SetMemory(0x58E574, Add, 0x00000053);
		SetMemory(0x58E578, Add, 0x00000030);
		SetMemory(0x58E57C, Add, 0x00000053);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFFA0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFFA0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFA0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFFA0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000053);
		SetMemory(0x58E574, Add, 0x00000030);
		SetMemory(0x58E578, Add, 0x00000053);
		SetMemory(0x58E57C, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFA0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFFA0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000005D);
		SetMemory(0x58E574, Add, 0x00000019);
		SetMemory(0x58E578, Add, 0x0000005D);
		SetMemory(0x58E57C, Add, 0x00000019);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFFA0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFFA0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000005D);
		SetMemory(0x58E574, Add, 0xFFFFFFE7);
		SetMemory(0x58E578, Add, 0x0000005D);
		SetMemory(0x58E57C, Add, 0xFFFFFFE7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0x00000044);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0x00000044);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000044);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0x00000044);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBC);
		SetMemory(0x58E574, Add, 0xFFFFFFBC);
		SetMemory(0x58E578, Add, 0xFFFFFFBC);
		SetMemory(0x58E57C, Add, 0xFFFFFFBC);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000053);
		SetMemory(0x58E574, Add, 0xFFFFFFD0);
		SetMemory(0x58E578, Add, 0x00000053);
		SetMemory(0x58E57C, Add, 0xFFFFFFD0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFFA0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFFA0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFA0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFFA0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillCount");
		Wait(1000);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(1300);
		RemoveUnit("50 + 1n Tank", CurrentPlayer);
		RemoveUnit("60 + 1n Danimoth", CurrentPlayer);
		RemoveUnit("40 + 1n Mojo", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("02.Chtholly_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "02.Chtholly_Bozo", CurrentPlayer);
		Order(" * Fenix", CurrentPlayer, "Anywhere", Move, "02.Chtholly_Bozo");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 231, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("02.Chtholly_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnit("Protoss Observer", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "02.Chtholly_Bozo", CurrentPlayer);
		Order(" * Fenix", CurrentPlayer, "Anywhere", Move, "02.Chtholly_Bozo");
		ModifyUnitShields(All, " * Fenix", CurrentPlayer, "Anywhere", 1);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000029);
		SetMemory(0x58E574, Add, 0x0000009B);
		SetMemory(0x58E578, Add, 0x00000029);
		SetMemory(0x58E57C, Add, 0x0000009B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000071);
		SetMemory(0x58E574, Add, 0x00000071);
		SetMemory(0x58E578, Add, 0x00000071);
		SetMemory(0x58E57C, Add, 0x00000071);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009B);
		SetMemory(0x58E574, Add, 0x00000029);
		SetMemory(0x58E578, Add, 0x0000009B);
		SetMemory(0x58E57C, Add, 0x00000029);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000009B);
		SetMemory(0x58E574, Add, 0xFFFFFFD7);
		SetMemory(0x58E578, Add, 0x0000009B);
		SetMemory(0x58E57C, Add, 0xFFFFFFD7);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000071);
		SetMemory(0x58E574, Add, 0xFFFFFF8F);
		SetMemory(0x58E578, Add, 0x00000071);
		SetMemory(0x58E57C, Add, 0xFFFFFF8F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0x0000008B);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0x0000008B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFB0);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0xFFFFFFB0);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000029);
		SetMemory(0x58E574, Add, 0xFFFFFF65);
		SetMemory(0x58E578, Add, 0x00000029);
		SetMemory(0x58E57C, Add, 0xFFFFFF65);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000008B);
		SetMemory(0x58E574, Add, 0x00000050);
		SetMemory(0x58E578, Add, 0x0000008B);
		SetMemory(0x58E57C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000050);
		SetMemory(0x58E574, Add, 0xFFFFFF75);
		SetMemory(0x58E578, Add, 0x00000050);
		SetMemory(0x58E57C, Add, 0xFFFFFF75);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF75);
		SetMemory(0x58E574, Add, 0xFFFFFFB0);
		SetMemory(0x58E578, Add, 0xFFFFFF75);
		SetMemory(0x58E57C, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(4, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(AllPlayers, SetTo, 2005, " `SkillText");
		SetDeaths(CurrentPlayer, SetTo, 9999, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0x000000B5);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0x000000B5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000B5);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0x000000B5);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF4B);
		SetMemory(0x58E574, Add, 0xFFFFFF4B);
		SetMemory(0x58E578, Add, 0xFFFFFF4B);
		SetMemory(0x58E57C, Add, 0xFFFFFF4B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF80);
		SetMemory(0x58E574, Add, 0x000000DE);
		SetMemory(0x58E578, Add, 0xFFFFFF80);
		SetMemory(0x58E57C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000DE);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E578, Add, 0x000000DE);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0xFFFFFF22);
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0xFFFFFF22);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF22);
		SetMemory(0x58E574, Add, 0xFFFFFF80);
		SetMemory(0x58E578, Add, 0xFFFFFF22);
		SetMemory(0x58E57C, Add, 0xFFFFFF80);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFBE);
		SetMemory(0x58E574, Add, 0x000000F7);
		SetMemory(0x58E578, Add, 0xFFFFFFBE);
		SetMemory(0x58E57C, Add, 0x000000F7);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000F7);
		SetMemory(0x58E574, Add, 0x00000042);
		SetMemory(0x58E578, Add, 0x000000F7);
		SetMemory(0x58E57C, Add, 0x00000042);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000042);
		SetMemory(0x58E574, Add, 0xFFFFFF09);
		SetMemory(0x58E578, Add, 0x00000042);
		SetMemory(0x58E57C, Add, 0xFFFFFF09);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF09);
		SetMemory(0x58E574, Add, 0xFFFFFFBE);
		SetMemory(0x58E578, Add, 0xFFFFFF09);
		SetMemory(0x58E57C, Add, 0xFFFFFFBE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 230, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 231, " `SkillStep");
		Wait(2000);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 2006, " `SkillText");
		Wait(5000);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 2007, " `SkillText");
		SetDeaths(CurrentPlayer, SetTo, 235, " `SkillStep");
		Wait(2500);
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

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		MoveLocation("02.Chtholly_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnit("Protoss Observer", CurrentPlayer);
		ModifyUnitShields(All, " * Fenix", CurrentPlayer, "Anywhere", 10);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(1000);
		SetDeaths(AllPlayers, SetTo, 2009, " `SkillText_Uiltimate");
		Wait(3500);
		SetDeaths(AllPlayers, SetTo, 2010, " `SkillText_Uiltimate");
		Wait(0);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Add, 0x00000020);
		SetMemory(0x58E57C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000020);
		SetMemory(0x58E570, Subtract, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000020);
		SetMemory(0x58E570, Add, 0x00000020);
		SetMemory(0x58E574, Subtract, 0x00000020);
		SetMemory(0x58E57C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000080);
		SetMemory(0x58E570, Add, 0x00000080);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000080);
		SetMemory(0x58E57C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000080);
		SetMemory(0x58E570, Subtract, 0x00000080);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000080);
		SetMemory(0x58E57C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000040);
		SetMemory(0x58E570, Add, 0x00000040);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000040);
		SetMemory(0x58E57C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000040);
		SetMemory(0x58E570, Subtract, 0x00000040);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000040);
		SetMemory(0x58E57C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(6, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(6, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000060);
		SetMemory(0x58E570, Add, 0x00000060);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000060);
		SetMemory(0x58E57C, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000060);
		SetMemory(0x58E570, Subtract, 0x00000060);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000060);
		SetMemory(0x58E57C, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(12, "40 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(12, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(12, "40 + 1n Marine", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(12, "40 + 1n Marine", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(12, "40 + 1n Marine", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(12, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x00000000);
		SetMemory(0x58E570, Subtract, 0x00000000);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(12, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x00000000);
		SetMemory(0x58E57C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(12, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(12, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Goliath", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Goliath", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Add, 0x000000C0);
		SetMemory(0x58E57C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Subtract, 0x000000C0);
		SetMemory(0x58E570, Subtract, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E578, Add, 0x000000C0);
		SetMemory(0x58E570, Add, 0x000000C0);
		SetMemory(0x58E574, Subtract, 0x000000C0);
		SetMemory(0x58E57C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(8, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF60);
		SetMemory(0x58E574, Add, 0x000000C8);
		SetMemory(0x58E578, Add, 0xFFFFFF60);
		SetMemory(0x58E57C, Add, 0x000000C8);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000C8);
		SetMemory(0x58E574, Add, 0x000000A0);
		SetMemory(0x58E578, Add, 0x000000C8);
		SetMemory(0x58E57C, Add, 0x000000A0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000A0);
		SetMemory(0x58E574, Add, 0xFFFFFF38);
		SetMemory(0x58E578, Add, 0x000000A0);
		SetMemory(0x58E57C, Add, 0xFFFFFF38);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF38);
		SetMemory(0x58E574, Add, 0xFFFFFF60);
		SetMemory(0x58E578, Add, 0xFFFFFF38);
		SetMemory(0x58E57C, Add, 0xFFFFFF60);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF91);
		SetMemory(0x58E574, Add, 0x000000E7);
		SetMemory(0x58E578, Add, 0xFFFFFF91);
		SetMemory(0x58E57C, Add, 0x000000E7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000E7);
		SetMemory(0x58E574, Add, 0x0000006F);
		SetMemory(0x58E578, Add, 0x000000E7);
		SetMemory(0x58E57C, Add, 0x0000006F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x0000006F);
		SetMemory(0x58E574, Add, 0xFFFFFF19);
		SetMemory(0x58E578, Add, 0x0000006F);
		SetMemory(0x58E57C, Add, 0xFFFFFF19);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF19);
		SetMemory(0x58E574, Add, 0xFFFFFF91);
		SetMemory(0x58E578, Add, 0xFFFFFF19);
		SetMemory(0x58E57C, Add, 0xFFFFFF91);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFFC7);
		SetMemory(0x58E574, Add, 0x000000FA);
		SetMemory(0x58E578, Add, 0xFFFFFFC7);
		SetMemory(0x58E57C, Add, 0x000000FA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x000000FA);
		SetMemory(0x58E574, Add, 0x00000039);
		SetMemory(0x58E578, Add, 0x000000FA);
		SetMemory(0x58E57C, Add, 0x00000039);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000039);
		SetMemory(0x58E574, Add, 0xFFFFFF06);
		SetMemory(0x58E578, Add, 0x00000039);
		SetMemory(0x58E57C, Add, 0xFFFFFF06);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF06);
		SetMemory(0x58E574, Add, 0xFFFFFFC7);
		SetMemory(0x58E578, Add, 0xFFFFFF06);
		SetMemory(0x58E57C, Add, 0xFFFFFFC7);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0x00000100);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0x00000100);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000100);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0x00000100);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0x00000000);
		SetMemory(0x58E574, Add, 0xFFFFFF00);
		SetMemory(0x58E578, Add, 0x00000000);
		SetMemory(0x58E57C, Add, 0xFFFFFF00);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E570, Add, 0xFFFFFF00);
		SetMemory(0x58E574, Add, 0x00000000);
		SetMemory(0x58E578, Add, 0xFFFFFF00);
		SetMemory(0x58E57C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "02.Chtholly");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, AtMost, 99, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		MoveLocation("02.Chtholly_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "02.Chtholly_Bozo");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		PreserveTrigger();
		Wait(1500);
		SetDeaths(CurrentPlayer, SetTo, 99, " `SkillCount");
		Wait(0);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P7);
		SetSwitch("JunkYardDog", Set);
		Wait(250);
		SetSwitch("JunkYardDog", Clear);
		Wait(1500);
		SetSwitch("JunkYardDog", Set);
		Wait(250);
		SetSwitch("JunkYardDog", Clear);
		Wait(1000);
		GiveUnits(All, "80 + 1n Artanis", P7, "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 100, " `SkillCount");
		Wait(0);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(3500);
		SetSwitch("Recall - Chtholly", Clear);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(800);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("UiltimateSwitch", Clear);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		PreserveTrigger();
		Wait(1500);
		SetDeaths(CurrentPlayer, SetTo, 99, " `SkillCount");
		Wait(0);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P8);
		SetSwitch("JunkYardDog", Set);
		Wait(250);
		SetSwitch("JunkYardDog", Clear);
		Wait(1500);
		SetSwitch("JunkYardDog", Set);
		Wait(250);
		SetSwitch("JunkYardDog", Clear);
		Wait(1000);
		GiveUnits(All, "80 + 1n Artanis", P8, "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 100, " `SkillCount");
		Wait(0);
		MoveLocation("02.Chtholly", " * Fenix", CurrentPlayer, "Anywhere");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "02.Chtholly");
		Wait(2500);
		SetSwitch("Recall - Chtholly", Clear);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(1800);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("UiltimateSwitch", Clear);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 999, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 240, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 2000, " `SkillText_Unique");
	},
}