Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 07.Cecillia
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2001, " * Fenix");
	},
	actions = {
		Comment("07.Cecillia");
		SetDeaths(AllPlayers, SetTo, 7, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 2000, " * Fenix");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("Unique - Ceilia", Set);
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\r\n\x13\x17O Skill \x04패시브를 \x06OFF \x04시킵니다.\r\n", 0);
		SetSwitch("Unique - Ceilia", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Switch("Unique - Ceilia", Cleared);
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		DisplayText("\r\n\x13\x17O Skill \x04패시브를 \x06ON \x04시킵니다.\r\n", 0);
		SetSwitch("Unique - Ceilia", Set);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(All, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 600, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(All, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 400, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 300, " `SkillStep");
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		Wait(500);
		SetResources(CurrentPlayer, Add, 300, Gas);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 200, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		Wait(500);
		SetResources(CurrentPlayer, Add, 200, Gas);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
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

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 450, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
		Accumulate(CurrentPlayer, AtLeast, 300, Gas);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 450, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Subtract, 300, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
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
		SetDeaths(AllPlayers, SetTo, 1000, " `SkillText2");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtMost, 14);
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 1010, " `SkillText2");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Subtract, 200, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 15);
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 1010, " `SkillText2");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Subtract, 200, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 1020, " `SkillText2");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Subtract, 300, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 1020, " `SkillText2");
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

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Switch("Unique - Ceilia", Set);
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Deaths(CurrentPlayer, AtLeast, 360, " `DeadCount");
		Deaths(CurrentPlayer, AtMost, 999, " `DeadCount");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 72, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 2880, " `UniqueCoolTime");
		SetDeaths(AllPlayers, SetTo, 7000, " `SkillText_Unique");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
		SetResources(CurrentPlayer, SetTo, 0, Gas);
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

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E778, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E778, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E778, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E778, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E778, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E778, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000032);
		SetMemory(0x58E778, Subtract, 0x00000032);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000032);
		SetMemory(0x58E784, Subtract, 0x00000032);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000032);
		SetMemory(0x58E778, Add, 0x00000032);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(50);
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

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(500);
		RemoveUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Subtract, 0x0000005F);
		SetMemory(0x58E784, Subtract, 0x0000005F);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000011);
		SetMemory(0x58E780, Subtract, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E77C, Add, 0x0000005F);
		SetMemory(0x58E784, Add, 0x0000005F);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Subtract, 0x0000005A);
		SetMemory(0x58E784, Subtract, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000021);
		SetMemory(0x58E780, Subtract, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000021);
		SetMemory(0x58E780, Add, 0x00000021);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Subtract, 0x0000004A);
		SetMemory(0x58E784, Subtract, 0x0000004A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000003E);
		SetMemory(0x58E780, Subtract, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000003E);
		SetMemory(0x58E780, Add, 0x0000003E);
		SetMemory(0x58E77C, Add, 0x0000004A);
		SetMemory(0x58E784, Add, 0x0000004A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Subtract, 0x0000003E);
		SetMemory(0x58E784, Subtract, 0x0000003E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004A);
		SetMemory(0x58E780, Subtract, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E77C, Add, 0x0000003E);
		SetMemory(0x58E784, Add, 0x0000003E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Subtract, 0x00000021);
		SetMemory(0x58E784, Subtract, 0x00000021);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005A);
		SetMemory(0x58E780, Subtract, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E77C, Add, 0x00000021);
		SetMemory(0x58E784, Add, 0x00000021);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Subtract, 0x00000011);
		SetMemory(0x58E784, Subtract, 0x00000011);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000005F);
		SetMemory(0x58E780, Subtract, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E77C, Add, 0x00000011);
		SetMemory(0x58E784, Add, 0x00000011);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E77C, Subtract, 0x00000020);
		SetMemory(0x58E784, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000020);
		SetMemory(0x58E780, Subtract, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000020);
		SetMemory(0x58E780, Add, 0x00000020);
		SetMemory(0x58E77C, Add, 0x00000020);
		SetMemory(0x58E784, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		SetMemory(0x58E77C, Subtract, 0x00000060);
		SetMemory(0x58E784, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000060);
		SetMemory(0x58E780, Subtract, 0x00000060);
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000060);
		SetMemory(0x58E780, Add, 0x00000060);
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(150);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "80 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Order("80 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		KillUnitAt(All, "80 + 1n Ghost", "Anywhere", CurrentPlayer);
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia_Bozo", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF5C);
		SetMemory(0x58E778, Add, 0xFFFFFF5C);
		SetMemory(0x58E77C, Add, 0x0000004B);
		SetMemory(0x58E784, Add, 0x0000004B);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6D);
		SetMemory(0x58E778, Add, 0xFFFFFF6D);
		SetMemory(0x58E77C, Add, 0xFFFFFF97);
		SetMemory(0x58E784, Add, 0xFFFFFF97);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E77C, Add, 0xFFFFFF4C);
		SetMemory(0x58E784, Add, 0xFFFFFF4C);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x000000A4);
		SetMemory(0x58E778, Add, 0x000000A4);
		SetMemory(0x58E77C, Add, 0xFFFFFFB5);
		SetMemory(0x58E784, Add, 0xFFFFFFB5);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000093);
		SetMemory(0x58E778, Add, 0x00000093);
		SetMemory(0x58E77C, Add, 0x00000069);
		SetMemory(0x58E784, Add, 0x00000069);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFEF);
		SetMemory(0x58E778, Add, 0xFFFFFFEF);
		SetMemory(0x58E77C, Add, 0x000000B4);
		SetMemory(0x58E784, Add, 0x000000B4);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFFF);
		SetMemory(0x58E778, Add, 0xFFFFFFFF);
		SetMemory(0x58E77C, Add, 0x0000005E);
		SetMemory(0x58E784, Add, 0x0000005E);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAE);
		SetMemory(0x58E778, Add, 0xFFFFFFAE);
		SetMemory(0x58E77C, Add, 0x0000002E);
		SetMemory(0x58E784, Add, 0x0000002E);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAF);
		SetMemory(0x58E778, Add, 0xFFFFFFAF);
		SetMemory(0x58E77C, Add, 0xFFFFFFD0);
		SetMemory(0x58E784, Add, 0xFFFFFFD0);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000001);
		SetMemory(0x58E778, Add, 0x00000001);
		SetMemory(0x58E77C, Add, 0xFFFFFFA2);
		SetMemory(0x58E784, Add, 0xFFFFFFA2);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000052);
		SetMemory(0x58E778, Add, 0x00000052);
		SetMemory(0x58E77C, Add, 0xFFFFFFD2);
		SetMemory(0x58E784, Add, 0xFFFFFFD2);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000051);
		SetMemory(0x58E778, Add, 0x00000051);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFF6);
		SetMemory(0x58E778, Add, 0xFFFFFFF6);
		SetMemory(0x58E77C, Add, 0x00000062);
		SetMemory(0x58E784, Add, 0x00000062);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFA6);
		SetMemory(0x58E778, Add, 0xFFFFFFA6);
		SetMemory(0x58E77C, Add, 0x00000028);
		SetMemory(0x58E784, Add, 0x00000028);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB0);
		SetMemory(0x58E778, Add, 0xFFFFFFB0);
		SetMemory(0x58E77C, Add, 0xFFFFFFC6);
		SetMemory(0x58E784, Add, 0xFFFFFFC6);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000000A);
		SetMemory(0x58E778, Add, 0x0000000A);
		SetMemory(0x58E77C, Add, 0xFFFFFF9E);
		SetMemory(0x58E784, Add, 0xFFFFFF9E);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E77C, Add, 0xFFFFFFD8);
		SetMemory(0x58E784, Add, 0xFFFFFFD8);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000050);
		SetMemory(0x58E778, Add, 0x00000050);
		SetMemory(0x58E77C, Add, 0x0000003A);
		SetMemory(0x58E784, Add, 0x0000003A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFEC);
		SetMemory(0x58E778, Add, 0xFFFFFFEC);
		SetMemory(0x58E77C, Add, 0x00000066);
		SetMemory(0x58E784, Add, 0x00000066);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF9E);
		SetMemory(0x58E778, Add, 0xFFFFFF9E);
		SetMemory(0x58E77C, Add, 0x00000022);
		SetMemory(0x58E784, Add, 0x00000022);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB2);
		SetMemory(0x58E778, Add, 0xFFFFFFB2);
		SetMemory(0x58E77C, Add, 0xFFFFFFBC);
		SetMemory(0x58E784, Add, 0xFFFFFFBC);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000014);
		SetMemory(0x58E778, Add, 0x00000014);
		SetMemory(0x58E77C, Add, 0xFFFFFF9A);
		SetMemory(0x58E784, Add, 0xFFFFFF9A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000062);
		SetMemory(0x58E778, Add, 0x00000062);
		SetMemory(0x58E77C, Add, 0xFFFFFFDE);
		SetMemory(0x58E784, Add, 0xFFFFFFDE);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004E);
		SetMemory(0x58E778, Add, 0x0000004E);
		SetMemory(0x58E77C, Add, 0x00000044);
		SetMemory(0x58E784, Add, 0x00000044);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFE1);
		SetMemory(0x58E778, Add, 0xFFFFFFE1);
		SetMemory(0x58E77C, Add, 0x00000069);
		SetMemory(0x58E784, Add, 0x00000069);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF96);
		SetMemory(0x58E778, Add, 0xFFFFFF96);
		SetMemory(0x58E77C, Add, 0x0000001A);
		SetMemory(0x58E784, Add, 0x0000001A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB5);
		SetMemory(0x58E778, Add, 0xFFFFFFB5);
		SetMemory(0x58E77C, Add, 0xFFFFFFB1);
		SetMemory(0x58E784, Add, 0xFFFFFFB1);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000001F);
		SetMemory(0x58E778, Add, 0x0000001F);
		SetMemory(0x58E77C, Add, 0xFFFFFF97);
		SetMemory(0x58E784, Add, 0xFFFFFF97);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000006A);
		SetMemory(0x58E778, Add, 0x0000006A);
		SetMemory(0x58E77C, Add, 0xFFFFFFE6);
		SetMemory(0x58E784, Add, 0xFFFFFFE6);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004B);
		SetMemory(0x58E778, Add, 0x0000004B);
		SetMemory(0x58E77C, Add, 0x0000004F);
		SetMemory(0x58E784, Add, 0x0000004F);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFD7);
		SetMemory(0x58E778, Add, 0xFFFFFFD7);
		SetMemory(0x58E77C, Add, 0x0000006C);
		SetMemory(0x58E784, Add, 0x0000006C);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF8E);
		SetMemory(0x58E778, Add, 0xFFFFFF8E);
		SetMemory(0x58E77C, Add, 0x00000012);
		SetMemory(0x58E784, Add, 0x00000012);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB7);
		SetMemory(0x58E778, Add, 0xFFFFFFB7);
		SetMemory(0x58E77C, Add, 0xFFFFFFA6);
		SetMemory(0x58E784, Add, 0xFFFFFFA6);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000029);
		SetMemory(0x58E778, Add, 0x00000029);
		SetMemory(0x58E77C, Add, 0xFFFFFF94);
		SetMemory(0x58E784, Add, 0xFFFFFF94);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000072);
		SetMemory(0x58E778, Add, 0x00000072);
		SetMemory(0x58E77C, Add, 0xFFFFFFEE);
		SetMemory(0x58E784, Add, 0xFFFFFFEE);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFCC);
		SetMemory(0x58E778, Add, 0xFFFFFFCC);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF88);
		SetMemory(0x58E778, Add, 0xFFFFFF88);
		SetMemory(0x58E77C, Add, 0x00000009);
		SetMemory(0x58E784, Add, 0x00000009);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFBC);
		SetMemory(0x58E778, Add, 0xFFFFFFBC);
		SetMemory(0x58E77C, Add, 0xFFFFFF9C);
		SetMemory(0x58E784, Add, 0xFFFFFF9C);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000034);
		SetMemory(0x58E778, Add, 0x00000034);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000078);
		SetMemory(0x58E778, Add, 0x00000078);
		SetMemory(0x58E77C, Add, 0xFFFFFFF7);
		SetMemory(0x58E784, Add, 0xFFFFFFF7);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000044);
		SetMemory(0x58E778, Add, 0x00000044);
		SetMemory(0x58E77C, Add, 0x00000064);
		SetMemory(0x58E784, Add, 0x00000064);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC1);
		SetMemory(0x58E778, Add, 0xFFFFFFC1);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF82);
		SetMemory(0x58E778, Add, 0xFFFFFF82);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC1);
		SetMemory(0x58E778, Add, 0xFFFFFFC1);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000003F);
		SetMemory(0x58E778, Add, 0x0000003F);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000007E);
		SetMemory(0x58E778, Add, 0x0000007E);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000003F);
		SetMemory(0x58E778, Add, 0x0000003F);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB6);
		SetMemory(0x58E778, Add, 0xFFFFFFB6);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF7D);
		SetMemory(0x58E778, Add, 0xFFFFFF7D);
		SetMemory(0x58E77C, Add, 0xFFFFFFF6);
		SetMemory(0x58E784, Add, 0xFFFFFFF6);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC7);
		SetMemory(0x58E778, Add, 0xFFFFFFC7);
		SetMemory(0x58E77C, Add, 0xFFFFFF89);
		SetMemory(0x58E784, Add, 0xFFFFFF89);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000083);
		SetMemory(0x58E778, Add, 0x00000083);
		SetMemory(0x58E77C, Add, 0x0000000A);
		SetMemory(0x58E784, Add, 0x0000000A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000039);
		SetMemory(0x58E778, Add, 0x00000039);
		SetMemory(0x58E77C, Add, 0x00000077);
		SetMemory(0x58E784, Add, 0x00000077);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAC);
		SetMemory(0x58E778, Add, 0xFFFFFFAC);
		SetMemory(0x58E77C, Add, 0x0000006C);
		SetMemory(0x58E784, Add, 0x0000006C);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF78);
		SetMemory(0x58E778, Add, 0xFFFFFF78);
		SetMemory(0x58E77C, Add, 0xFFFFFFED);
		SetMemory(0x58E784, Add, 0xFFFFFFED);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFCC);
		SetMemory(0x58E778, Add, 0xFFFFFFCC);
		SetMemory(0x58E77C, Add, 0xFFFFFF81);
		SetMemory(0x58E784, Add, 0xFFFFFF81);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000054);
		SetMemory(0x58E778, Add, 0x00000054);
		SetMemory(0x58E77C, Add, 0xFFFFFF94);
		SetMemory(0x58E784, Add, 0xFFFFFF94);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000088);
		SetMemory(0x58E778, Add, 0x00000088);
		SetMemory(0x58E77C, Add, 0x00000013);
		SetMemory(0x58E784, Add, 0x00000013);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000034);
		SetMemory(0x58E778, Add, 0x00000034);
		SetMemory(0x58E77C, Add, 0x0000007F);
		SetMemory(0x58E784, Add, 0x0000007F);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFA1);
		SetMemory(0x58E778, Add, 0xFFFFFFA1);
		SetMemory(0x58E77C, Add, 0x0000006A);
		SetMemory(0x58E784, Add, 0x0000006A);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF75);
		SetMemory(0x58E778, Add, 0xFFFFFF75);
		SetMemory(0x58E77C, Add, 0xFFFFFFE3);
		SetMemory(0x58E784, Add, 0xFFFFFFE3);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFD4);
		SetMemory(0x58E778, Add, 0xFFFFFFD4);
		SetMemory(0x58E77C, Add, 0xFFFFFF79);
		SetMemory(0x58E784, Add, 0xFFFFFF79);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E77C, Add, 0xFFFFFF96);
		SetMemory(0x58E784, Add, 0xFFFFFF96);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000008B);
		SetMemory(0x58E778, Add, 0x0000008B);
		SetMemory(0x58E77C, Add, 0x0000001D);
		SetMemory(0x58E784, Add, 0x0000001D);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000002C);
		SetMemory(0x58E778, Add, 0x0000002C);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(6, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF96);
		SetMemory(0x58E778, Add, 0xFFFFFF96);
		SetMemory(0x58E77C, Add, 0x00000067);
		SetMemory(0x58E784, Add, 0x00000067);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF72);
		SetMemory(0x58E778, Add, 0xFFFFFF72);
		SetMemory(0x58E77C, Add, 0xFFFFFFD8);
		SetMemory(0x58E784, Add, 0xFFFFFFD8);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFDC);
		SetMemory(0x58E778, Add, 0xFFFFFFDC);
		SetMemory(0x58E77C, Add, 0xFFFFFF71);
		SetMemory(0x58E784, Add, 0xFFFFFF71);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000006A);
		SetMemory(0x58E778, Add, 0x0000006A);
		SetMemory(0x58E77C, Add, 0xFFFFFF99);
		SetMemory(0x58E784, Add, 0xFFFFFF99);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000008E);
		SetMemory(0x58E778, Add, 0x0000008E);
		SetMemory(0x58E77C, Add, 0x00000028);
		SetMemory(0x58E784, Add, 0x00000028);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000024);
		SetMemory(0x58E778, Add, 0x00000024);
		SetMemory(0x58E77C, Add, 0x0000008F);
		SetMemory(0x58E784, Add, 0x0000008F);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000100);
		SetMemory(0x58E784, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000100);
		SetMemory(0x58E784, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000100);
		SetMemory(0x58E784, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000100);
		SetMemory(0x58E784, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000100);
		SetMemory(0x58E780, Add, 0x00000100);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000100);
		SetMemory(0x58E780, Subtract, 0x00000100);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000100);
		SetMemory(0x58E780, Add, 0x00000100);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000100);
		SetMemory(0x58E780, Subtract, 0x00000100);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000100);
		SetMemory(0x58E784, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000100);
		SetMemory(0x58E784, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000100);
		SetMemory(0x58E784, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000100);
		SetMemory(0x58E784, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000100);
		SetMemory(0x58E780, Add, 0x00000100);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000100);
		SetMemory(0x58E780, Subtract, 0x00000100);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000100);
		SetMemory(0x58E780, Add, 0x00000100);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000100);
		SetMemory(0x58E780, Subtract, 0x00000100);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		Wait(300);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(230);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000030);
		SetMemory(0x58E784, Subtract, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000030);
		SetMemory(0x58E780, Subtract, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000030);
		SetMemory(0x58E780, Add, 0x00000030);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(40);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 7000, " `SkillText_Uiltimate");
		SetSwitch("Recall - Ceilia", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000005);
		SetMemory(0x58E778, Add, 0x00000005);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB5);
		SetMemory(0x58E778, Add, 0xFFFFFFB5);
		SetMemory(0x58E77C, Add, 0x00000031);
		SetMemory(0x58E784, Add, 0x00000031);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB0);
		SetMemory(0x58E778, Add, 0xFFFFFFB0);
		SetMemory(0x58E77C, Add, 0xFFFFFFD7);
		SetMemory(0x58E784, Add, 0xFFFFFFD7);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFFB);
		SetMemory(0x58E778, Add, 0xFFFFFFFB);
		SetMemory(0x58E77C, Add, 0xFFFFFFA6);
		SetMemory(0x58E784, Add, 0xFFFFFFA6);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004B);
		SetMemory(0x58E778, Add, 0x0000004B);
		SetMemory(0x58E77C, Add, 0xFFFFFFCF);
		SetMemory(0x58E784, Add, 0xFFFFFFCF);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000050);
		SetMemory(0x58E778, Add, 0x00000050);
		SetMemory(0x58E77C, Add, 0x00000029);
		SetMemory(0x58E784, Add, 0x00000029);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF65);
		SetMemory(0x58E778, Add, 0xFFFFFF65);
		SetMemory(0x58E77C, Add, 0x00000051);
		SetMemory(0x58E784, Add, 0x00000051);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6C);
		SetMemory(0x58E778, Add, 0xFFFFFF6C);
		SetMemory(0x58E77C, Add, 0xFFFFFFA2);
		SetMemory(0x58E784, Add, 0xFFFFFFA2);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000007);
		SetMemory(0x58E778, Add, 0x00000007);
		SetMemory(0x58E77C, Add, 0xFFFFFF51);
		SetMemory(0x58E784, Add, 0xFFFFFF51);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000009B);
		SetMemory(0x58E778, Add, 0x0000009B);
		SetMemory(0x58E77C, Add, 0xFFFFFFAF);
		SetMemory(0x58E784, Add, 0xFFFFFFAF);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000094);
		SetMemory(0x58E778, Add, 0x00000094);
		SetMemory(0x58E77C, Add, 0x0000005E);
		SetMemory(0x58E784, Add, 0x0000005E);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFF9);
		SetMemory(0x58E778, Add, 0xFFFFFFF9);
		SetMemory(0x58E77C, Add, 0x000000AF);
		SetMemory(0x58E784, Add, 0x000000AF);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6F);
		SetMemory(0x58E778, Add, 0xFFFFFF6F);
		SetMemory(0x58E77C, Add, 0x00000057);
		SetMemory(0x58E784, Add, 0x00000057);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6C);
		SetMemory(0x58E778, Add, 0xFFFFFF6C);
		SetMemory(0x58E77C, Add, 0xFFFFFFAE);
		SetMemory(0x58E784, Add, 0xFFFFFFAE);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFFD);
		SetMemory(0x58E778, Add, 0xFFFFFFFD);
		SetMemory(0x58E77C, Add, 0xFFFFFF57);
		SetMemory(0x58E784, Add, 0xFFFFFF57);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000091);
		SetMemory(0x58E778, Add, 0x00000091);
		SetMemory(0x58E77C, Add, 0xFFFFFFA9);
		SetMemory(0x58E784, Add, 0xFFFFFFA9);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000094);
		SetMemory(0x58E778, Add, 0x00000094);
		SetMemory(0x58E77C, Add, 0x00000052);
		SetMemory(0x58E784, Add, 0x00000052);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000003);
		SetMemory(0x58E778, Add, 0x00000003);
		SetMemory(0x58E77C, Add, 0x000000A9);
		SetMemory(0x58E784, Add, 0x000000A9);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF78);
		SetMemory(0x58E778, Add, 0xFFFFFF78);
		SetMemory(0x58E77C, Add, 0x0000005C);
		SetMemory(0x58E784, Add, 0x0000005C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6C);
		SetMemory(0x58E778, Add, 0xFFFFFF6C);
		SetMemory(0x58E77C, Add, 0xFFFFFFB8);
		SetMemory(0x58E784, Add, 0xFFFFFFB8);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFF4);
		SetMemory(0x58E778, Add, 0xFFFFFFF4);
		SetMemory(0x58E77C, Add, 0xFFFFFF5C);
		SetMemory(0x58E784, Add, 0xFFFFFF5C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000088);
		SetMemory(0x58E778, Add, 0x00000088);
		SetMemory(0x58E77C, Add, 0xFFFFFFA4);
		SetMemory(0x58E784, Add, 0xFFFFFFA4);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000094);
		SetMemory(0x58E778, Add, 0x00000094);
		SetMemory(0x58E77C, Add, 0x00000048);
		SetMemory(0x58E784, Add, 0x00000048);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000000C);
		SetMemory(0x58E778, Add, 0x0000000C);
		SetMemory(0x58E77C, Add, 0x000000A4);
		SetMemory(0x58E784, Add, 0x000000A4);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF82);
		SetMemory(0x58E778, Add, 0xFFFFFF82);
		SetMemory(0x58E77C, Add, 0x00000060);
		SetMemory(0x58E784, Add, 0x00000060);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6E);
		SetMemory(0x58E778, Add, 0xFFFFFF6E);
		SetMemory(0x58E77C, Add, 0xFFFFFFC3);
		SetMemory(0x58E784, Add, 0xFFFFFFC3);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFEC);
		SetMemory(0x58E778, Add, 0xFFFFFFEC);
		SetMemory(0x58E77C, Add, 0xFFFFFF63);
		SetMemory(0x58E784, Add, 0xFFFFFF63);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000007E);
		SetMemory(0x58E778, Add, 0x0000007E);
		SetMemory(0x58E77C, Add, 0xFFFFFFA0);
		SetMemory(0x58E784, Add, 0xFFFFFFA0);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000092);
		SetMemory(0x58E778, Add, 0x00000092);
		SetMemory(0x58E77C, Add, 0x0000003D);
		SetMemory(0x58E784, Add, 0x0000003D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000014);
		SetMemory(0x58E778, Add, 0x00000014);
		SetMemory(0x58E77C, Add, 0x0000009D);
		SetMemory(0x58E784, Add, 0x0000009D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF8C);
		SetMemory(0x58E778, Add, 0xFFFFFF8C);
		SetMemory(0x58E77C, Add, 0x00000064);
		SetMemory(0x58E784, Add, 0x00000064);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6F);
		SetMemory(0x58E778, Add, 0xFFFFFF6F);
		SetMemory(0x58E77C, Add, 0xFFFFFFCE);
		SetMemory(0x58E784, Add, 0xFFFFFFCE);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFE3);
		SetMemory(0x58E778, Add, 0xFFFFFFE3);
		SetMemory(0x58E77C, Add, 0xFFFFFF6A);
		SetMemory(0x58E784, Add, 0xFFFFFF6A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000074);
		SetMemory(0x58E778, Add, 0x00000074);
		SetMemory(0x58E77C, Add, 0xFFFFFF9C);
		SetMemory(0x58E784, Add, 0xFFFFFF9C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000091);
		SetMemory(0x58E778, Add, 0x00000091);
		SetMemory(0x58E77C, Add, 0x00000032);
		SetMemory(0x58E784, Add, 0x00000032);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000001D);
		SetMemory(0x58E778, Add, 0x0000001D);
		SetMemory(0x58E77C, Add, 0x00000096);
		SetMemory(0x58E784, Add, 0x00000096);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF96);
		SetMemory(0x58E778, Add, 0xFFFFFF96);
		SetMemory(0x58E77C, Add, 0x00000067);
		SetMemory(0x58E784, Add, 0x00000067);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF72);
		SetMemory(0x58E778, Add, 0xFFFFFF72);
		SetMemory(0x58E77C, Add, 0xFFFFFFD8);
		SetMemory(0x58E784, Add, 0xFFFFFFD8);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFDC);
		SetMemory(0x58E778, Add, 0xFFFFFFDC);
		SetMemory(0x58E77C, Add, 0xFFFFFF71);
		SetMemory(0x58E784, Add, 0xFFFFFF71);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000006A);
		SetMemory(0x58E778, Add, 0x0000006A);
		SetMemory(0x58E77C, Add, 0xFFFFFF99);
		SetMemory(0x58E784, Add, 0xFFFFFF99);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000008E);
		SetMemory(0x58E778, Add, 0x0000008E);
		SetMemory(0x58E77C, Add, 0x00000028);
		SetMemory(0x58E784, Add, 0x00000028);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000024);
		SetMemory(0x58E778, Add, 0x00000024);
		SetMemory(0x58E77C, Add, 0x0000008F);
		SetMemory(0x58E784, Add, 0x0000008F);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFA1);
		SetMemory(0x58E778, Add, 0xFFFFFFA1);
		SetMemory(0x58E77C, Add, 0x0000006A);
		SetMemory(0x58E784, Add, 0x0000006A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF75);
		SetMemory(0x58E778, Add, 0xFFFFFF75);
		SetMemory(0x58E77C, Add, 0xFFFFFFE3);
		SetMemory(0x58E784, Add, 0xFFFFFFE3);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFD4);
		SetMemory(0x58E778, Add, 0xFFFFFFD4);
		SetMemory(0x58E77C, Add, 0xFFFFFF79);
		SetMemory(0x58E784, Add, 0xFFFFFF79);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000005F);
		SetMemory(0x58E778, Add, 0x0000005F);
		SetMemory(0x58E77C, Add, 0xFFFFFF96);
		SetMemory(0x58E784, Add, 0xFFFFFF96);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000008B);
		SetMemory(0x58E778, Add, 0x0000008B);
		SetMemory(0x58E77C, Add, 0x0000001D);
		SetMemory(0x58E784, Add, 0x0000001D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000002C);
		SetMemory(0x58E778, Add, 0x0000002C);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAC);
		SetMemory(0x58E778, Add, 0xFFFFFFAC);
		SetMemory(0x58E77C, Add, 0x0000006C);
		SetMemory(0x58E784, Add, 0x0000006C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF78);
		SetMemory(0x58E778, Add, 0xFFFFFF78);
		SetMemory(0x58E77C, Add, 0xFFFFFFED);
		SetMemory(0x58E784, Add, 0xFFFFFFED);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFCC);
		SetMemory(0x58E778, Add, 0xFFFFFFCC);
		SetMemory(0x58E77C, Add, 0xFFFFFF81);
		SetMemory(0x58E784, Add, 0xFFFFFF81);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000054);
		SetMemory(0x58E778, Add, 0x00000054);
		SetMemory(0x58E77C, Add, 0xFFFFFF94);
		SetMemory(0x58E784, Add, 0xFFFFFF94);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000088);
		SetMemory(0x58E778, Add, 0x00000088);
		SetMemory(0x58E77C, Add, 0x00000013);
		SetMemory(0x58E784, Add, 0x00000013);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000034);
		SetMemory(0x58E778, Add, 0x00000034);
		SetMemory(0x58E77C, Add, 0x0000007F);
		SetMemory(0x58E784, Add, 0x0000007F);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB6);
		SetMemory(0x58E778, Add, 0xFFFFFFB6);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF7D);
		SetMemory(0x58E778, Add, 0xFFFFFF7D);
		SetMemory(0x58E77C, Add, 0xFFFFFFF6);
		SetMemory(0x58E784, Add, 0xFFFFFFF6);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC7);
		SetMemory(0x58E778, Add, 0xFFFFFFC7);
		SetMemory(0x58E77C, Add, 0xFFFFFF89);
		SetMemory(0x58E784, Add, 0xFFFFFF89);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004A);
		SetMemory(0x58E778, Add, 0x0000004A);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000083);
		SetMemory(0x58E778, Add, 0x00000083);
		SetMemory(0x58E77C, Add, 0x0000000A);
		SetMemory(0x58E784, Add, 0x0000000A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000039);
		SetMemory(0x58E778, Add, 0x00000039);
		SetMemory(0x58E77C, Add, 0x00000077);
		SetMemory(0x58E784, Add, 0x00000077);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC1);
		SetMemory(0x58E778, Add, 0xFFFFFFC1);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF82);
		SetMemory(0x58E778, Add, 0xFFFFFF82);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFC1);
		SetMemory(0x58E778, Add, 0xFFFFFFC1);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000003F);
		SetMemory(0x58E778, Add, 0x0000003F);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000007E);
		SetMemory(0x58E778, Add, 0x0000007E);
		SetMemory(0x58E77C, Add, 0x00000000);
		SetMemory(0x58E784, Add, 0x00000000);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000003F);
		SetMemory(0x58E778, Add, 0x0000003F);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFCC);
		SetMemory(0x58E778, Add, 0xFFFFFFCC);
		SetMemory(0x58E77C, Add, 0x0000006D);
		SetMemory(0x58E784, Add, 0x0000006D);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF88);
		SetMemory(0x58E778, Add, 0xFFFFFF88);
		SetMemory(0x58E77C, Add, 0x00000009);
		SetMemory(0x58E784, Add, 0x00000009);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFBC);
		SetMemory(0x58E778, Add, 0xFFFFFFBC);
		SetMemory(0x58E77C, Add, 0xFFFFFF9C);
		SetMemory(0x58E784, Add, 0xFFFFFF9C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000034);
		SetMemory(0x58E778, Add, 0x00000034);
		SetMemory(0x58E77C, Add, 0xFFFFFF93);
		SetMemory(0x58E784, Add, 0xFFFFFF93);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000078);
		SetMemory(0x58E778, Add, 0x00000078);
		SetMemory(0x58E77C, Add, 0xFFFFFFF7);
		SetMemory(0x58E784, Add, 0xFFFFFFF7);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000044);
		SetMemory(0x58E778, Add, 0x00000044);
		SetMemory(0x58E77C, Add, 0x00000064);
		SetMemory(0x58E784, Add, 0x00000064);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFD7);
		SetMemory(0x58E778, Add, 0xFFFFFFD7);
		SetMemory(0x58E77C, Add, 0x0000006C);
		SetMemory(0x58E784, Add, 0x0000006C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF8E);
		SetMemory(0x58E778, Add, 0xFFFFFF8E);
		SetMemory(0x58E77C, Add, 0x00000012);
		SetMemory(0x58E784, Add, 0x00000012);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB7);
		SetMemory(0x58E778, Add, 0xFFFFFFB7);
		SetMemory(0x58E77C, Add, 0xFFFFFFA6);
		SetMemory(0x58E784, Add, 0xFFFFFFA6);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000029);
		SetMemory(0x58E778, Add, 0x00000029);
		SetMemory(0x58E77C, Add, 0xFFFFFF94);
		SetMemory(0x58E784, Add, 0xFFFFFF94);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000072);
		SetMemory(0x58E778, Add, 0x00000072);
		SetMemory(0x58E77C, Add, 0xFFFFFFEE);
		SetMemory(0x58E784, Add, 0xFFFFFFEE);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E77C, Add, 0x0000005A);
		SetMemory(0x58E784, Add, 0x0000005A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFE1);
		SetMemory(0x58E778, Add, 0xFFFFFFE1);
		SetMemory(0x58E77C, Add, 0x00000069);
		SetMemory(0x58E784, Add, 0x00000069);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF96);
		SetMemory(0x58E778, Add, 0xFFFFFF96);
		SetMemory(0x58E77C, Add, 0x0000001A);
		SetMemory(0x58E784, Add, 0x0000001A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB5);
		SetMemory(0x58E778, Add, 0xFFFFFFB5);
		SetMemory(0x58E77C, Add, 0xFFFFFFB1);
		SetMemory(0x58E784, Add, 0xFFFFFFB1);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000001F);
		SetMemory(0x58E778, Add, 0x0000001F);
		SetMemory(0x58E77C, Add, 0xFFFFFF97);
		SetMemory(0x58E784, Add, 0xFFFFFF97);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000006A);
		SetMemory(0x58E778, Add, 0x0000006A);
		SetMemory(0x58E77C, Add, 0xFFFFFFE6);
		SetMemory(0x58E784, Add, 0xFFFFFFE6);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004B);
		SetMemory(0x58E778, Add, 0x0000004B);
		SetMemory(0x58E77C, Add, 0x0000004F);
		SetMemory(0x58E784, Add, 0x0000004F);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFEC);
		SetMemory(0x58E778, Add, 0xFFFFFFEC);
		SetMemory(0x58E77C, Add, 0x00000066);
		SetMemory(0x58E784, Add, 0x00000066);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF9E);
		SetMemory(0x58E778, Add, 0xFFFFFF9E);
		SetMemory(0x58E77C, Add, 0x00000022);
		SetMemory(0x58E784, Add, 0x00000022);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB2);
		SetMemory(0x58E778, Add, 0xFFFFFFB2);
		SetMemory(0x58E77C, Add, 0xFFFFFFBC);
		SetMemory(0x58E784, Add, 0xFFFFFFBC);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000014);
		SetMemory(0x58E778, Add, 0x00000014);
		SetMemory(0x58E77C, Add, 0xFFFFFF9A);
		SetMemory(0x58E784, Add, 0xFFFFFF9A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000062);
		SetMemory(0x58E778, Add, 0x00000062);
		SetMemory(0x58E77C, Add, 0xFFFFFFDE);
		SetMemory(0x58E784, Add, 0xFFFFFFDE);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000004E);
		SetMemory(0x58E778, Add, 0x0000004E);
		SetMemory(0x58E77C, Add, 0x00000044);
		SetMemory(0x58E784, Add, 0x00000044);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFF6);
		SetMemory(0x58E778, Add, 0xFFFFFFF6);
		SetMemory(0x58E77C, Add, 0x00000062);
		SetMemory(0x58E784, Add, 0x00000062);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFA6);
		SetMemory(0x58E778, Add, 0xFFFFFFA6);
		SetMemory(0x58E77C, Add, 0x00000028);
		SetMemory(0x58E784, Add, 0x00000028);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFB0);
		SetMemory(0x58E778, Add, 0xFFFFFFB0);
		SetMemory(0x58E77C, Add, 0xFFFFFFC6);
		SetMemory(0x58E784, Add, 0xFFFFFFC6);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000000A);
		SetMemory(0x58E778, Add, 0x0000000A);
		SetMemory(0x58E77C, Add, 0xFFFFFF9E);
		SetMemory(0x58E784, Add, 0xFFFFFF9E);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x0000005A);
		SetMemory(0x58E778, Add, 0x0000005A);
		SetMemory(0x58E77C, Add, 0xFFFFFFD8);
		SetMemory(0x58E784, Add, 0xFFFFFFD8);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000050);
		SetMemory(0x58E778, Add, 0x00000050);
		SetMemory(0x58E77C, Add, 0x0000003A);
		SetMemory(0x58E784, Add, 0x0000003A);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFFF);
		SetMemory(0x58E778, Add, 0xFFFFFFFF);
		SetMemory(0x58E77C, Add, 0x0000005E);
		SetMemory(0x58E784, Add, 0x0000005E);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAE);
		SetMemory(0x58E778, Add, 0xFFFFFFAE);
		SetMemory(0x58E77C, Add, 0x0000002E);
		SetMemory(0x58E784, Add, 0x0000002E);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFAF);
		SetMemory(0x58E778, Add, 0xFFFFFFAF);
		SetMemory(0x58E77C, Add, 0xFFFFFFD0);
		SetMemory(0x58E784, Add, 0xFFFFFFD0);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000001);
		SetMemory(0x58E778, Add, 0x00000001);
		SetMemory(0x58E77C, Add, 0xFFFFFFA2);
		SetMemory(0x58E784, Add, 0xFFFFFFA2);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000052);
		SetMemory(0x58E778, Add, 0x00000052);
		SetMemory(0x58E77C, Add, 0xFFFFFFD2);
		SetMemory(0x58E784, Add, 0xFFFFFFD2);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000051);
		SetMemory(0x58E778, Add, 0x00000051);
		SetMemory(0x58E77C, Add, 0x00000030);
		SetMemory(0x58E784, Add, 0x00000030);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(6, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF5C);
		SetMemory(0x58E778, Add, 0xFFFFFF5C);
		SetMemory(0x58E77C, Add, 0x0000004B);
		SetMemory(0x58E784, Add, 0x0000004B);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFF6D);
		SetMemory(0x58E778, Add, 0xFFFFFF6D);
		SetMemory(0x58E77C, Add, 0xFFFFFF97);
		SetMemory(0x58E784, Add, 0xFFFFFF97);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000011);
		SetMemory(0x58E778, Add, 0x00000011);
		SetMemory(0x58E77C, Add, 0xFFFFFF4C);
		SetMemory(0x58E784, Add, 0xFFFFFF4C);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x000000A4);
		SetMemory(0x58E778, Add, 0x000000A4);
		SetMemory(0x58E77C, Add, 0xFFFFFFB5);
		SetMemory(0x58E784, Add, 0xFFFFFFB5);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0x00000093);
		SetMemory(0x58E778, Add, 0x00000093);
		SetMemory(0x58E77C, Add, 0x00000069);
		SetMemory(0x58E784, Add, 0x00000069);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E780, Add, 0xFFFFFFEF);
		SetMemory(0x58E778, Add, 0xFFFFFFEF);
		SetMemory(0x58E77C, Add, 0x000000B4);
		SetMemory(0x58E784, Add, 0x000000B4);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		SetSwitch("Recall - Ceilia", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000002D);
		SetMemory(0x58E780, Add, 0x0000002D);
		SetMemory(0x58E77C, Subtract, 0x0000002D);
		SetMemory(0x58E784, Subtract, 0x0000002D);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000002D);
		SetMemory(0x58E780, Subtract, 0x0000002D);
		SetMemory(0x58E77C, Subtract, 0x0000002D);
		SetMemory(0x58E784, Subtract, 0x0000002D);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000002D);
		SetMemory(0x58E780, Subtract, 0x0000002D);
		SetMemory(0x58E77C, Add, 0x0000002D);
		SetMemory(0x58E784, Add, 0x0000002D);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000002D);
		SetMemory(0x58E780, Add, 0x0000002D);
		SetMemory(0x58E77C, Add, 0x0000002D);
		SetMemory(0x58E784, Add, 0x0000002D);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000080);
		SetMemory(0x58E780, Add, 0x00000080);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000080);
		SetMemory(0x58E784, Subtract, 0x00000080);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000080);
		SetMemory(0x58E780, Subtract, 0x00000080);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000080);
		SetMemory(0x58E784, Add, 0x00000080);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000006E);
		SetMemory(0x58E780, Add, 0x0000006E);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000006E);
		SetMemory(0x58E780, Subtract, 0x0000006E);
		SetMemory(0x58E77C, Subtract, 0x00000040);
		SetMemory(0x58E784, Subtract, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000006E);
		SetMemory(0x58E780, Subtract, 0x0000006E);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000006E);
		SetMemory(0x58E780, Add, 0x0000006E);
		SetMemory(0x58E77C, Add, 0x00000040);
		SetMemory(0x58E784, Add, 0x00000040);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x0000006E);
		SetMemory(0x58E784, Subtract, 0x0000006E);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Subtract, 0x0000006E);
		SetMemory(0x58E784, Subtract, 0x0000006E);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000040);
		SetMemory(0x58E780, Subtract, 0x00000040);
		SetMemory(0x58E77C, Add, 0x0000006E);
		SetMemory(0x58E784, Add, 0x0000006E);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000040);
		SetMemory(0x58E780, Add, 0x00000040);
		SetMemory(0x58E77C, Add, 0x0000006E);
		SetMemory(0x58E784, Add, 0x0000006E);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000C0);
		SetMemory(0x58E780, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x000000C0);
		SetMemory(0x58E784, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000C0);
		SetMemory(0x58E780, Subtract, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x000000C0);
		SetMemory(0x58E784, Add, 0x000000C0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Subtract, 0x00000049);
		SetMemory(0x58E784, Subtract, 0x00000049);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000B1);
		SetMemory(0x58E780, Subtract, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000B1);
		SetMemory(0x58E780, Add, 0x000000B1);
		SetMemory(0x58E77C, Add, 0x00000049);
		SetMemory(0x58E784, Add, 0x00000049);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Subtract, 0x000000B1);
		SetMemory(0x58E784, Subtract, 0x000000B1);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000049);
		SetMemory(0x58E780, Subtract, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000049);
		SetMemory(0x58E780, Add, 0x00000049);
		SetMemory(0x58E77C, Add, 0x000000B1);
		SetMemory(0x58E784, Add, 0x000000B1);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Subtract, 0x00000087);
		SetMemory(0x58E784, Subtract, 0x00000087);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000087);
		SetMemory(0x58E780, Subtract, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000087);
		SetMemory(0x58E780, Add, 0x00000087);
		SetMemory(0x58E77C, Add, 0x00000087);
		SetMemory(0x58E784, Add, 0x00000087);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000100);
		SetMemory(0x58E780, Add, 0x00000100);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000100);
		SetMemory(0x58E784, Subtract, 0x00000100);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000100);
		SetMemory(0x58E780, Subtract, 0x00000100);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000100);
		SetMemory(0x58E784, Add, 0x00000100);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000F3);
		SetMemory(0x58E780, Add, 0x000000F3);
		SetMemory(0x58E77C, Subtract, 0x0000004F);
		SetMemory(0x58E784, Subtract, 0x0000004F);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000F3);
		SetMemory(0x58E780, Subtract, 0x000000F3);
		SetMemory(0x58E77C, Subtract, 0x0000004F);
		SetMemory(0x58E784, Subtract, 0x0000004F);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000F3);
		SetMemory(0x58E780, Subtract, 0x000000F3);
		SetMemory(0x58E77C, Add, 0x0000004F);
		SetMemory(0x58E784, Add, 0x0000004F);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000F3);
		SetMemory(0x58E780, Add, 0x000000F3);
		SetMemory(0x58E77C, Add, 0x0000004F);
		SetMemory(0x58E784, Add, 0x0000004F);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004F);
		SetMemory(0x58E780, Add, 0x0000004F);
		SetMemory(0x58E77C, Subtract, 0x000000F3);
		SetMemory(0x58E784, Subtract, 0x000000F3);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004F);
		SetMemory(0x58E780, Subtract, 0x0000004F);
		SetMemory(0x58E77C, Subtract, 0x000000F3);
		SetMemory(0x58E784, Subtract, 0x000000F3);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000004F);
		SetMemory(0x58E780, Subtract, 0x0000004F);
		SetMemory(0x58E77C, Add, 0x000000F3);
		SetMemory(0x58E784, Add, 0x000000F3);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000004F);
		SetMemory(0x58E780, Add, 0x0000004F);
		SetMemory(0x58E77C, Add, 0x000000F3);
		SetMemory(0x58E784, Add, 0x000000F3);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000CF);
		SetMemory(0x58E780, Add, 0x000000CF);
		SetMemory(0x58E77C, Subtract, 0x00000096);
		SetMemory(0x58E784, Subtract, 0x00000096);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000CF);
		SetMemory(0x58E780, Subtract, 0x000000CF);
		SetMemory(0x58E77C, Subtract, 0x00000096);
		SetMemory(0x58E784, Subtract, 0x00000096);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000CF);
		SetMemory(0x58E780, Subtract, 0x000000CF);
		SetMemory(0x58E77C, Add, 0x00000096);
		SetMemory(0x58E784, Add, 0x00000096);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000CF);
		SetMemory(0x58E780, Add, 0x000000CF);
		SetMemory(0x58E77C, Add, 0x00000096);
		SetMemory(0x58E784, Add, 0x00000096);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000096);
		SetMemory(0x58E780, Add, 0x00000096);
		SetMemory(0x58E77C, Subtract, 0x000000CF);
		SetMemory(0x58E784, Subtract, 0x000000CF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000096);
		SetMemory(0x58E780, Subtract, 0x00000096);
		SetMemory(0x58E77C, Subtract, 0x000000CF);
		SetMemory(0x58E784, Subtract, 0x000000CF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000096);
		SetMemory(0x58E780, Subtract, 0x00000096);
		SetMemory(0x58E77C, Add, 0x000000CF);
		SetMemory(0x58E784, Add, 0x000000CF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000096);
		SetMemory(0x58E780, Add, 0x00000096);
		SetMemory(0x58E77C, Add, 0x000000CF);
		SetMemory(0x58E784, Add, 0x000000CF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000140);
		SetMemory(0x58E780, Add, 0x00000140);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000140);
		SetMemory(0x58E784, Subtract, 0x00000140);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000140);
		SetMemory(0x58E780, Subtract, 0x00000140);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000140);
		SetMemory(0x58E784, Add, 0x00000140);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000135);
		SetMemory(0x58E780, Add, 0x00000135);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000135);
		SetMemory(0x58E780, Subtract, 0x00000135);
		SetMemory(0x58E77C, Subtract, 0x00000053);
		SetMemory(0x58E784, Subtract, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000135);
		SetMemory(0x58E780, Subtract, 0x00000135);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000135);
		SetMemory(0x58E780, Add, 0x00000135);
		SetMemory(0x58E77C, Add, 0x00000053);
		SetMemory(0x58E784, Add, 0x00000053);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000135);
		SetMemory(0x58E784, Subtract, 0x00000135);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Subtract, 0x00000135);
		SetMemory(0x58E784, Subtract, 0x00000135);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000053);
		SetMemory(0x58E780, Subtract, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000135);
		SetMemory(0x58E784, Add, 0x00000135);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000053);
		SetMemory(0x58E780, Add, 0x00000053);
		SetMemory(0x58E77C, Add, 0x00000135);
		SetMemory(0x58E784, Add, 0x00000135);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000115);
		SetMemory(0x58E780, Add, 0x00000115);
		SetMemory(0x58E77C, Subtract, 0x000000A0);
		SetMemory(0x58E784, Subtract, 0x000000A0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000115);
		SetMemory(0x58E780, Subtract, 0x00000115);
		SetMemory(0x58E77C, Subtract, 0x000000A0);
		SetMemory(0x58E784, Subtract, 0x000000A0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000115);
		SetMemory(0x58E780, Subtract, 0x00000115);
		SetMemory(0x58E77C, Add, 0x000000A0);
		SetMemory(0x58E784, Add, 0x000000A0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000115);
		SetMemory(0x58E780, Add, 0x00000115);
		SetMemory(0x58E77C, Add, 0x000000A0);
		SetMemory(0x58E784, Add, 0x000000A0);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000A0);
		SetMemory(0x58E780, Add, 0x000000A0);
		SetMemory(0x58E77C, Subtract, 0x00000115);
		SetMemory(0x58E784, Subtract, 0x00000115);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000A0);
		SetMemory(0x58E780, Subtract, 0x000000A0);
		SetMemory(0x58E77C, Subtract, 0x00000115);
		SetMemory(0x58E784, Subtract, 0x00000115);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000A0);
		SetMemory(0x58E780, Subtract, 0x000000A0);
		SetMemory(0x58E77C, Add, 0x00000115);
		SetMemory(0x58E784, Add, 0x00000115);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000A0);
		SetMemory(0x58E780, Add, 0x000000A0);
		SetMemory(0x58E77C, Add, 0x00000115);
		SetMemory(0x58E784, Add, 0x00000115);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000E2);
		SetMemory(0x58E780, Add, 0x000000E2);
		SetMemory(0x58E77C, Subtract, 0x000000E2);
		SetMemory(0x58E784, Subtract, 0x000000E2);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000E2);
		SetMemory(0x58E780, Subtract, 0x000000E2);
		SetMemory(0x58E77C, Subtract, 0x000000E2);
		SetMemory(0x58E784, Subtract, 0x000000E2);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000E2);
		SetMemory(0x58E780, Subtract, 0x000000E2);
		SetMemory(0x58E77C, Add, 0x000000E2);
		SetMemory(0x58E784, Add, 0x000000E2);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000E2);
		SetMemory(0x58E780, Add, 0x000000E2);
		SetMemory(0x58E77C, Add, 0x000000E2);
		SetMemory(0x58E784, Add, 0x000000E2);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000180);
		SetMemory(0x58E780, Add, 0x00000180);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Subtract, 0x00000180);
		SetMemory(0x58E784, Subtract, 0x00000180);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000180);
		SetMemory(0x58E780, Subtract, 0x00000180);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E77C, Add, 0x00000180);
		SetMemory(0x58E784, Add, 0x00000180);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000176);
		SetMemory(0x58E780, Add, 0x00000176);
		SetMemory(0x58E77C, Subtract, 0x00000055);
		SetMemory(0x58E784, Subtract, 0x00000055);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000176);
		SetMemory(0x58E780, Subtract, 0x00000176);
		SetMemory(0x58E77C, Subtract, 0x00000055);
		SetMemory(0x58E784, Subtract, 0x00000055);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000176);
		SetMemory(0x58E780, Subtract, 0x00000176);
		SetMemory(0x58E77C, Add, 0x00000055);
		SetMemory(0x58E784, Add, 0x00000055);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000176);
		SetMemory(0x58E780, Add, 0x00000176);
		SetMemory(0x58E77C, Add, 0x00000055);
		SetMemory(0x58E784, Add, 0x00000055);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000055);
		SetMemory(0x58E780, Add, 0x00000055);
		SetMemory(0x58E77C, Subtract, 0x00000176);
		SetMemory(0x58E784, Subtract, 0x00000176);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000055);
		SetMemory(0x58E780, Subtract, 0x00000055);
		SetMemory(0x58E77C, Subtract, 0x00000176);
		SetMemory(0x58E784, Subtract, 0x00000176);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000055);
		SetMemory(0x58E780, Subtract, 0x00000055);
		SetMemory(0x58E77C, Add, 0x00000176);
		SetMemory(0x58E784, Add, 0x00000176);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000055);
		SetMemory(0x58E780, Add, 0x00000055);
		SetMemory(0x58E77C, Add, 0x00000176);
		SetMemory(0x58E784, Add, 0x00000176);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000159);
		SetMemory(0x58E780, Add, 0x00000159);
		SetMemory(0x58E77C, Subtract, 0x000000A6);
		SetMemory(0x58E784, Subtract, 0x000000A6);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000159);
		SetMemory(0x58E780, Subtract, 0x00000159);
		SetMemory(0x58E77C, Subtract, 0x000000A6);
		SetMemory(0x58E784, Subtract, 0x000000A6);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x00000159);
		SetMemory(0x58E780, Subtract, 0x00000159);
		SetMemory(0x58E77C, Add, 0x000000A6);
		SetMemory(0x58E784, Add, 0x000000A6);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x00000159);
		SetMemory(0x58E780, Add, 0x00000159);
		SetMemory(0x58E77C, Add, 0x000000A6);
		SetMemory(0x58E784, Add, 0x000000A6);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000A6);
		SetMemory(0x58E780, Add, 0x000000A6);
		SetMemory(0x58E77C, Subtract, 0x00000159);
		SetMemory(0x58E784, Subtract, 0x00000159);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000A6);
		SetMemory(0x58E780, Subtract, 0x000000A6);
		SetMemory(0x58E77C, Subtract, 0x00000159);
		SetMemory(0x58E784, Subtract, 0x00000159);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000A6);
		SetMemory(0x58E780, Subtract, 0x000000A6);
		SetMemory(0x58E77C, Add, 0x00000159);
		SetMemory(0x58E784, Add, 0x00000159);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000A6);
		SetMemory(0x58E780, Add, 0x000000A6);
		SetMemory(0x58E77C, Add, 0x00000159);
		SetMemory(0x58E784, Add, 0x00000159);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000012C);
		SetMemory(0x58E780, Add, 0x0000012C);
		SetMemory(0x58E77C, Subtract, 0x000000EF);
		SetMemory(0x58E784, Subtract, 0x000000EF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000012C);
		SetMemory(0x58E780, Subtract, 0x0000012C);
		SetMemory(0x58E77C, Subtract, 0x000000EF);
		SetMemory(0x58E784, Subtract, 0x000000EF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x0000012C);
		SetMemory(0x58E780, Subtract, 0x0000012C);
		SetMemory(0x58E77C, Add, 0x000000EF);
		SetMemory(0x58E784, Add, 0x000000EF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x0000012C);
		SetMemory(0x58E780, Add, 0x0000012C);
		SetMemory(0x58E77C, Add, 0x000000EF);
		SetMemory(0x58E784, Add, 0x000000EF);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Goliath", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000EF);
		SetMemory(0x58E780, Add, 0x000000EF);
		SetMemory(0x58E77C, Subtract, 0x0000012C);
		SetMemory(0x58E784, Subtract, 0x0000012C);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000EF);
		SetMemory(0x58E780, Subtract, 0x000000EF);
		SetMemory(0x58E77C, Subtract, 0x0000012C);
		SetMemory(0x58E784, Subtract, 0x0000012C);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Subtract, 0x000000EF);
		SetMemory(0x58E780, Subtract, 0x000000EF);
		SetMemory(0x58E77C, Add, 0x0000012C);
		SetMemory(0x58E784, Add, 0x0000012C);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		SetMemory(0x58E778, Add, 0x000000EF);
		SetMemory(0x58E780, Add, 0x000000EF);
		SetMemory(0x58E77C, Add, 0x0000012C);
		SetMemory(0x58E784, Add, 0x0000012C);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveUnit(8, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "07.Cecillia");
		MoveLocation("07.Cecillia", " * Fenix", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("60 + 3n Ghost", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "07.Cecillia");
		Wait(0);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Fenix");
		Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		Wait(230);
		KillUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}