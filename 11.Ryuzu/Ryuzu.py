
Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 12.Ryuzu
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Devouring One");
	},
	actions = {
		Comment("12.Ryuzu");
		SetDeaths(AllPlayers, SetTo, 12, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 1000, " * Devouring One");
		CreateUnit(1, " * Devouring One", "[Select]Select Unit", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 12000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		SetSwitch("Recall - Ryuzu", Set);
		Wait(1700);
		SetDeaths(AllPlayers, SetTo, 12001, " `SkillText_Unique");
		Wait(1000);
		SetDeaths(AllPlayers, SetTo, 12002, " `SkillText_Unique");
		Wait(1000);
		SetDeaths(AllPlayers, SetTo, 12003, " `SkillText_Unique");
		Wait(1400);
		SetDeaths(AllPlayers, SetTo, 12004, " `SkillText_Unique");
		Wait(1700);
		SetDeaths(AllPlayers, SetTo, 12005, " `SkillText_Unique");
		Wait(1600);
		SetDeaths(AllPlayers, SetTo, 12006, " `SkillText_Unique");
		Wait(2000);
		SetSwitch("Recall - Ryuzu", Clear);
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillStep");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 240, " `UniqueSkill");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
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
		SetDeaths(AllPlayers, SetTo, 6000, " `SkillText2");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 120, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 6002, " `SkillText2");
		KillUnitAt(3, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 6010, " `SkillText2");
		KillUnitAt(3, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 500, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 500, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 12000, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetSwitch("Recall - Alther", Set);
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
		Deaths(Foes, Exactly, 1000, " * Devouring One");
		Bring(Foes, AtLeast, 1, " * Devouring One", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "[Unique]Ryuzu");
		Deaths(Foes, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 6, " `SystemDebuff_Slow");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		MoveLocation("[Unique]Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}