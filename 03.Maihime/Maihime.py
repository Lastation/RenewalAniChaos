

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 03.Maihime
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1001, " * Dark Templar");
	},
	actions = {
		Comment("03.Maihime");
		SetDeaths(AllPlayers, SetTo, 3, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 1000, " * Dark Templar");
		CreateUnit(1, " * Dark Templar", "[Select]Select Unit", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(P1, Add, 200, Gas);
		SetResources(P2, Add, 200, Gas);
		SetResources(P3, Add, 200, Gas);
		SetDeaths(AllPlayers, SetTo, 3000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 720, " `UniqueCoolTime");
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(P4, Add, 200, Gas);
		SetResources(P5, Add, 200, Gas);
		SetResources(P6, Add, 200, Gas);
		SetDeaths(AllPlayers, SetTo, 3000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 720, " `UniqueCoolTime");
		CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 110, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 3300, " `SkillText");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 3000, " `SkillText");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 220, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 3001, " `SkillText");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		MoveLocation("02.Chtholly", " * Dark Templar", CurrentPlayer, "Anywhere");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
		Accumulate(CurrentPlayer, AtLeast, 500, Gas);
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(AllPlayers, SetTo, 3100, " `SkillText");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Subtract, 500, Gas);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
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
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 3200, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 250, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Cleared);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 250, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 330, " `SkillStep");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 3201, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("Recall - MaiHime", Set);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 250, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Set);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 600, Gas);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(6, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(6, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x0000005C);
		SetMemory(0x58E5C0, Add, 0x0000005C);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x0000002E);
		SetMemory(0x58E5C0, Add, 0x0000002E);
		SetMemory(0x58E5C4, Add, 0x00000050);
		SetMemory(0x58E5CC, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x0000002E);
		SetMemory(0x58E5C0, Subtract, 0x0000002E);
		SetMemory(0x58E5C4, Add, 0x00000050);
		SetMemory(0x58E5CC, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x0000005C);
		SetMemory(0x58E5C0, Subtract, 0x0000005C);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x0000002E);
		SetMemory(0x58E5C0, Subtract, 0x0000002E);
		SetMemory(0x58E5C4, Subtract, 0x00000050);
		SetMemory(0x58E5CC, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x0000002E);
		SetMemory(0x58E5C0, Add, 0x0000002E);
		SetMemory(0x58E5C4, Subtract, 0x00000050);
		SetMemory(0x58E5CC, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(230);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Move, "03.Maihime");
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(100);
		KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(9, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(9, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(50);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(150);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		Wait(30);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 32, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 34, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 2, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 36, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 37, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 38, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		Wait(230);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 39, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 40, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 41, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 42, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 43, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 44, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 45, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 46, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 47, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 48, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 49, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 50, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 51, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 52, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 53, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(5, "80 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(90);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(180);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000F0);
		SetMemory(0x58E5CC, Add, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000F0);
		SetMemory(0x58E5C0, Subtract, 0x000000F0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000F0);
		SetMemory(0x58E5CC, Subtract, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000F0);
		SetMemory(0x58E5C0, Add, 0x000000F0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Wait(1900);
		SetDeaths(AllPlayers, SetTo, 3002, " `SkillText");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 32, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 34, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 35, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 36, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 37, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 38, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 39, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 40, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(200);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 41, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 42, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 43, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 44, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 45, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 46, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 47, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(60);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 48, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 49, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(0);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 50, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(300);
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

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("03.Maihime_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "03.Maihime_Bozo");
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 1);
		SetAllianceStatus(P7, Ally);
		SetAllianceStatus(P8, Ally);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 18, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		MoveLocation("03.Maihime_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime_Bozo");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 18, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 20, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		MoveLocation("03.Maihime_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime_Bozo");
		MoveUnit(All, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime_Bozo");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		Wait(300);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
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
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(400);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000F0);
		SetMemory(0x58E5C0, Add, 0x000000F0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000F0);
		SetMemory(0x58E5CC, Add, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000F0);
		SetMemory(0x58E5C0, Subtract, 0x000000F0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000F0);
		SetMemory(0x58E5CC, Subtract, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000D0);
		SetMemory(0x58E5C0, Add, 0x000000D0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000D0);
		SetMemory(0x58E5CC, Add, 0x000000D0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000D0);
		SetMemory(0x58E5C0, Subtract, 0x000000D0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000D0);
		SetMemory(0x58E5CC, Subtract, 0x000000D0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000B0);
		SetMemory(0x58E5C0, Add, 0x000000B0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000B0);
		SetMemory(0x58E5CC, Add, 0x000000B0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000B0);
		SetMemory(0x58E5C0, Subtract, 0x000000B0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000B0);
		SetMemory(0x58E5CC, Subtract, 0x000000B0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000070);
		SetMemory(0x58E5C0, Subtract, 0x00000070);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000070);
		SetMemory(0x58E5CC, Subtract, 0x00000070);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000050);
		SetMemory(0x58E5C0, Add, 0x00000050);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000050);
		SetMemory(0x58E5CC, Add, 0x00000050);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000050);
		SetMemory(0x58E5C0, Subtract, 0x00000050);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000050);
		SetMemory(0x58E5CC, Subtract, 0x00000050);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000010);
		SetMemory(0x58E5C0, Add, 0x00000010);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000010);
		SetMemory(0x58E5CC, Add, 0x00000010);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000010);
		SetMemory(0x58E5C0, Subtract, 0x00000010);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000010);
		SetMemory(0x58E5CC, Subtract, 0x00000010);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000010);
		SetMemory(0x58E5CC, Add, 0x00000010);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000010);
		SetMemory(0x58E5C0, Subtract, 0x00000010);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000010);
		SetMemory(0x58E5CC, Subtract, 0x00000010);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000010);
		SetMemory(0x58E5C0, Add, 0x00000010);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000030);
		SetMemory(0x58E5CC, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000030);
		SetMemory(0x58E5C0, Subtract, 0x00000030);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000030);
		SetMemory(0x58E5CC, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000030);
		SetMemory(0x58E5C0, Add, 0x00000030);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000050);
		SetMemory(0x58E5CC, Add, 0x00000050);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000050);
		SetMemory(0x58E5C0, Subtract, 0x00000050);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000050);
		SetMemory(0x58E5CC, Subtract, 0x00000050);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000050);
		SetMemory(0x58E5C0, Add, 0x00000050);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000070);
		SetMemory(0x58E5C0, Subtract, 0x00000070);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000070);
		SetMemory(0x58E5CC, Subtract, 0x00000070);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000090);
		SetMemory(0x58E5C0, Subtract, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x00000090);
		SetMemory(0x58E5CC, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000B0);
		SetMemory(0x58E5CC, Add, 0x000000B0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000B0);
		SetMemory(0x58E5C0, Subtract, 0x000000B0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000B0);
		SetMemory(0x58E5CC, Subtract, 0x000000B0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000B0);
		SetMemory(0x58E5C0, Add, 0x000000B0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000D0);
		SetMemory(0x58E5CC, Add, 0x000000D0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000D0);
		SetMemory(0x58E5C0, Subtract, 0x000000D0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000D0);
		SetMemory(0x58E5CC, Subtract, 0x000000D0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000D0);
		SetMemory(0x58E5C0, Add, 0x000000D0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnitWithProperties(4, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x000000F0);
		SetMemory(0x58E5CC, Add, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000F0);
		SetMemory(0x58E5C0, Subtract, 0x000000F0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000110);
		SetMemory(0x58E5C0, Subtract, 0x00000110);
		SetMemory(0x58E5C4, Subtract, 0x000000F0);
		SetMemory(0x58E5CC, Subtract, 0x000000F0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000F0);
		SetMemory(0x58E5C0, Add, 0x000000F0);
		SetMemory(0x58E5C4, Subtract, 0x00000110);
		SetMemory(0x58E5CC, Subtract, 0x00000110);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P12);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "Uraj Crystal", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "Uraj Crystal", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Uraj Crystal", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(800);
		SetDeaths(AllPlayers, SetTo, 3101, " `SkillText");
		SetDeaths(CurrentPlayer, SetTo, 18, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000080);
		SetMemory(0x58E5C0, Subtract, 0x00000080);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000100);
		SetMemory(0x58E5C0, Subtract, 0x00000100);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000080);
		SetMemory(0x58E5C0, Add, 0x00000080);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000100);
		SetMemory(0x58E5C0, Add, 0x00000100);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000120);
		SetMemory(0x58E5CC, Add, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000100);
		SetMemory(0x58E5CC, Add, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x000000A0);
		SetMemory(0x58E5CC, Add, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000080);
		SetMemory(0x58E5CC, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000120);
		SetMemory(0x58E5C0, Add, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000120);
		SetMemory(0x58E5CC, Subtract, 0x00000120);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000100);
		SetMemory(0x58E5CC, Subtract, 0x00000100);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000A0);
		SetMemory(0x58E5C0, Add, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x000000E0);
		SetMemory(0x58E5CC, Subtract, 0x000000E0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x000000A0);
		SetMemory(0x58E5CC, Subtract, 0x000000A0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 18, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		SetDeaths(AllPlayers, SetTo, 3102, " `SkillText");
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(5, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000080);
		SetMemory(0x58E5CC, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000A0);
		SetMemory(0x58E5C0, Subtract, 0x000000A0);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000E0);
		SetMemory(0x58E5C0, Subtract, 0x000000E0);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000120);
		SetMemory(0x58E5C0, Subtract, 0x00000120);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Wait(90);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		GiveUnits(All, "60 + 1n Siege", P12, "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x000000C0);
		SetMemory(0x58E5C0, Subtract, 0x000000C0);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x000000C0);
		SetMemory(0x58E5CC, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000060);
		SetMemory(0x58E5C0, Add, 0x00000060);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000060);
		SetMemory(0x58E5CC, Add, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000060);
		SetMemory(0x58E5C0, Subtract, 0x00000060);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000060);
		SetMemory(0x58E5CC, Subtract, 0x00000060);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(230);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillStep");
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Uraj Crystal", "Anywhere", CurrentPlayer);
		Wait(0);
		SetAllianceStatus(P8, Enemy);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Combo
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillStep");
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Uraj Crystal", "Anywhere", CurrentPlayer);
		Wait(0);
		SetAllianceStatus(P7, Enemy);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 20);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFF20);
		SetMemory(0x58E5CC, Add, 0xFFFFFF20);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF20);
		SetMemory(0x58E5C8, Add, 0xFFFFFF20);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x000000DD);
		SetMemory(0x58E5CC, Add, 0x000000DD);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000DD);
		SetMemory(0x58E5C8, Add, 0x000000DD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFF23);
		SetMemory(0x58E5CC, Add, 0xFFFFFF23);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF23);
		SetMemory(0x58E5C8, Add, 0xFFFFFF23);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000004D);
		SetMemory(0x58E5C8, Add, 0x0000004D);
		SetMemory(0x58E5C4, Add, 0x000000D2);
		SetMemory(0x58E5CC, Add, 0x000000D2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000D2);
		SetMemory(0x58E5C8, Add, 0x000000D2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFB3);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C4, Add, 0xFFFFFF2E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF2E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C4, Add, 0x0000004D);
		SetMemory(0x58E5CC, Add, 0x0000004D);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C4, Add, 0x000000C2);
		SetMemory(0x58E5CC, Add, 0x000000C2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C2);
		SetMemory(0x58E5C8, Add, 0x000000C2);
		SetMemory(0x58E5C4, Add, 0xFFFFFF90);
		SetMemory(0x58E5CC, Add, 0xFFFFFF90);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF90);
		SetMemory(0x58E5C8, Add, 0xFFFFFF90);
		SetMemory(0x58E5C4, Add, 0xFFFFFF3E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF3E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000AC);
		SetMemory(0x58E5CC, Add, 0x000000AC);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000AC);
		SetMemory(0x58E5C8, Add, 0x000000AC);
		SetMemory(0x58E5C4, Add, 0xFFFFFF70);
		SetMemory(0x58E5CC, Add, 0xFFFFFF70);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF70);
		SetMemory(0x58E5C8, Add, 0xFFFFFF70);
		SetMemory(0x58E5C4, Add, 0xFFFFFF54);
		SetMemory(0x58E5CC, Add, 0xFFFFFF54);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF54);
		SetMemory(0x58E5C8, Add, 0xFFFFFF54);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000AC);
		SetMemory(0x58E5C8, Add, 0x000000AC);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0xFFFFFF54);
		SetMemory(0x58E5CC, Add, 0xFFFFFF54);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF54);
		SetMemory(0x58E5C8, Add, 0xFFFFFF54);
		SetMemory(0x58E5C4, Add, 0xFFFFFF70);
		SetMemory(0x58E5CC, Add, 0xFFFFFF70);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF70);
		SetMemory(0x58E5C8, Add, 0xFFFFFF70);
		SetMemory(0x58E5C4, Add, 0x000000AC);
		SetMemory(0x58E5CC, Add, 0x000000AC);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C2);
		SetMemory(0x58E5C8, Add, 0x000000C2);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C4, Add, 0xFFFFFF3E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF3E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C4, Add, 0xFFFFFF90);
		SetMemory(0x58E5CC, Add, 0xFFFFFF90);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF90);
		SetMemory(0x58E5C8, Add, 0xFFFFFF90);
		SetMemory(0x58E5C4, Add, 0x000000C2);
		SetMemory(0x58E5CC, Add, 0x000000C2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000D2);
		SetMemory(0x58E5C8, Add, 0x000000D2);
		SetMemory(0x58E5C4, Add, 0x0000004D);
		SetMemory(0x58E5CC, Add, 0x0000004D);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000004D);
		SetMemory(0x58E5C8, Add, 0x0000004D);
		SetMemory(0x58E5C4, Add, 0xFFFFFF2E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF2E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFB3);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C4, Add, 0x000000D2);
		SetMemory(0x58E5CC, Add, 0x000000D2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000DD);
		SetMemory(0x58E5C8, Add, 0x000000DD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFF23);
		SetMemory(0x58E5CC, Add, 0xFFFFFF23);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF23);
		SetMemory(0x58E5C8, Add, 0xFFFFFF23);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x000000DD);
		SetMemory(0x58E5CC, Add, 0x000000DD);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000E0);
		SetMemory(0x58E5C8, Add, 0x000000E0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFF20);
		SetMemory(0x58E5CC, Add, 0xFFFFFF20);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF20);
		SetMemory(0x58E5C8, Add, 0xFFFFFF20);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x000000E0);
		SetMemory(0x58E5CC, Add, 0x000000E0);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000DD);
		SetMemory(0x58E5C8, Add, 0x000000DD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFF23);
		SetMemory(0x58E5CC, Add, 0xFFFFFF23);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF23);
		SetMemory(0x58E5C8, Add, 0xFFFFFF23);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x000000DD);
		SetMemory(0x58E5CC, Add, 0x000000DD);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000D2);
		SetMemory(0x58E5C8, Add, 0x000000D2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFB3);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C4, Add, 0xFFFFFF2E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF2E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C4, Add, 0x0000004D);
		SetMemory(0x58E5CC, Add, 0x0000004D);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000004D);
		SetMemory(0x58E5C8, Add, 0x0000004D);
		SetMemory(0x58E5C4, Add, 0x000000D2);
		SetMemory(0x58E5CC, Add, 0x000000D2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C2);
		SetMemory(0x58E5C8, Add, 0x000000C2);
		SetMemory(0x58E5C4, Add, 0xFFFFFF90);
		SetMemory(0x58E5CC, Add, 0xFFFFFF90);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF90);
		SetMemory(0x58E5C8, Add, 0xFFFFFF90);
		SetMemory(0x58E5C4, Add, 0xFFFFFF3E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF3E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C4, Add, 0x000000C2);
		SetMemory(0x58E5CC, Add, 0x000000C2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000AC);
		SetMemory(0x58E5C8, Add, 0x000000AC);
		SetMemory(0x58E5C4, Add, 0xFFFFFF70);
		SetMemory(0x58E5CC, Add, 0xFFFFFF70);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF70);
		SetMemory(0x58E5C8, Add, 0xFFFFFF70);
		SetMemory(0x58E5C4, Add, 0xFFFFFF54);
		SetMemory(0x58E5CC, Add, 0xFFFFFF54);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF54);
		SetMemory(0x58E5C8, Add, 0xFFFFFF54);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0x000000AC);
		SetMemory(0x58E5CC, Add, 0x000000AC);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000090);
		SetMemory(0x58E5C8, Add, 0x00000090);
		SetMemory(0x58E5C4, Add, 0xFFFFFF54);
		SetMemory(0x58E5CC, Add, 0xFFFFFF54);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF54);
		SetMemory(0x58E5C8, Add, 0xFFFFFF54);
		SetMemory(0x58E5C4, Add, 0xFFFFFF70);
		SetMemory(0x58E5CC, Add, 0xFFFFFF70);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF70);
		SetMemory(0x58E5C8, Add, 0xFFFFFF70);
		SetMemory(0x58E5C4, Add, 0x000000AC);
		SetMemory(0x58E5CC, Add, 0x000000AC);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000AC);
		SetMemory(0x58E5C8, Add, 0x000000AC);
		SetMemory(0x58E5C4, Add, 0x00000090);
		SetMemory(0x58E5CC, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000070);
		SetMemory(0x58E5C8, Add, 0x00000070);
		SetMemory(0x58E5C4, Add, 0xFFFFFF3E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF3E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF3E);
		SetMemory(0x58E5C4, Add, 0xFFFFFF90);
		SetMemory(0x58E5CC, Add, 0xFFFFFF90);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF90);
		SetMemory(0x58E5C8, Add, 0xFFFFFF90);
		SetMemory(0x58E5C4, Add, 0x000000C2);
		SetMemory(0x58E5CC, Add, 0x000000C2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C2);
		SetMemory(0x58E5C8, Add, 0x000000C2);
		SetMemory(0x58E5C4, Add, 0x00000070);
		SetMemory(0x58E5CC, Add, 0x00000070);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000004D);
		SetMemory(0x58E5C8, Add, 0x0000004D);
		SetMemory(0x58E5C4, Add, 0xFFFFFF2E);
		SetMemory(0x58E5CC, Add, 0xFFFFFF2E);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C8, Add, 0xFFFFFF2E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFB3);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFB3);
		SetMemory(0x58E5C4, Add, 0x000000D2);
		SetMemory(0x58E5CC, Add, 0x000000D2);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000D2);
		SetMemory(0x58E5C8, Add, 0x000000D2);
		SetMemory(0x58E5C4, Add, 0x0000004D);
		SetMemory(0x58E5CC, Add, 0x0000004D);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFF23);
		SetMemory(0x58E5CC, Add, 0xFFFFFF23);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF23);
		SetMemory(0x58E5C8, Add, 0xFFFFFF23);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x000000DD);
		SetMemory(0x58E5CC, Add, 0x000000DD);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000DD);
		SetMemory(0x58E5C8, Add, 0x000000DD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		CreateUnit(8, "80 + 1n Vulture", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		CreateUnit(8, "80 + 1n Vulture", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		CreateUnit(8, "80 + 1n Vulture", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		CreateUnit(8, "80 + 1n Vulture", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 3n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zergling", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zergling", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", "60 + 1n Danimoth", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		MoveUnit(1, "60 + 3n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Bengalaas (Jungle)", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000000);
		SetMemory(0x58E5C0, Subtract, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000000);
		SetMemory(0x58E5CC, Subtract, 0x00000000);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Decorate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Decorate");
		PreserveTrigger();
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000040);
		SetMemory(0x58E5C0, Subtract, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Subtract, 0x00000020);
		SetMemory(0x58E5C0, Subtract, 0x00000020);
		SetMemory(0x58E5C4, Subtract, 0x00000040);
		SetMemory(0x58E5CC, Subtract, 0x00000040);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C4, Subtract, 0x00000020);
		SetMemory(0x58E5CC, Subtract, 0x00000020);
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("60 + 3n Ghost", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "03.Maihime");
		Wait(30);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("03.Maihime_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "03.Maihime_Bozo");
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 1);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000053);
		SetMemory(0x58E5C8, Add, 0x00000053);
		SetMemory(0x58E5C4, Add, 0x00000177);
		SetMemory(0x58E5CC, Add, 0x00000177);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C8, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C4, Add, 0xFFFFFEF0);
		SetMemory(0x58E5CC, Add, 0xFFFFFEF0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C8, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEF2);
		SetMemory(0x58E5C8, Add, 0xFFFFFEF2);
		SetMemory(0x58E5C4, Add, 0x00000111);
		SetMemory(0x58E5CC, Add, 0x00000111);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF16);
		SetMemory(0x58E5C8, Add, 0xFFFFFF16);
		SetMemory(0x58E5C4, Add, 0xFFFFFECF);
		SetMemory(0x58E5CC, Add, 0xFFFFFECF);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFECF);
		SetMemory(0x58E5C8, Add, 0xFFFFFECF);
		SetMemory(0x58E5C4, Add, 0x000000EA);
		SetMemory(0x58E5CC, Add, 0x000000EA);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000EA);
		SetMemory(0x58E5C8, Add, 0x000000EA);
		SetMemory(0x58E5C4, Add, 0x00000131);
		SetMemory(0x58E5CC, Add, 0x00000131);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE88);
		SetMemory(0x58E5C8, Add, 0xFFFFFE88);
		SetMemory(0x58E5C4, Add, 0xFFFFFFB0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFB0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF40);
		SetMemory(0x58E5C8, Add, 0xFFFFFF40);
		SetMemory(0x58E5C4, Add, 0xFFFFFEB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFEB3);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFEB3);
		SetMemory(0x58E5C4, Add, 0x000000C0);
		SetMemory(0x58E5CC, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0x0000014D);
		SetMemory(0x58E5CC, Add, 0x0000014D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF79);
		SetMemory(0x58E5C8, Add, 0xFFFFFF79);
		SetMemory(0x58E5C4, Add, 0xFFFFFE99);
		SetMemory(0x58E5CC, Add, 0xFFFFFE99);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF6D);
		SetMemory(0x58E5C8, Add, 0xFFFFFF6D);
		SetMemory(0x58E5C4, Add, 0xFFFFFE9D);
		SetMemory(0x58E5CC, Add, 0xFFFFFE9D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE9D);
		SetMemory(0x58E5C8, Add, 0xFFFFFE9D);
		SetMemory(0x58E5C4, Add, 0x00000093);
		SetMemory(0x58E5CC, Add, 0x00000093);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000093);
		SetMemory(0x58E5C8, Add, 0x00000093);
		SetMemory(0x58E5C4, Add, 0x00000163);
		SetMemory(0x58E5CC, Add, 0x00000163);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000E5);
		SetMemory(0x58E5C8, Add, 0x000000E5);
		SetMemory(0x58E5C4, Add, 0xFFFFFECC);
		SetMemory(0x58E5CC, Add, 0xFFFFFECC);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF9D);
		SetMemory(0x58E5C8, Add, 0xFFFFFF9D);
		SetMemory(0x58E5C4, Add, 0xFFFFFE8D);
		SetMemory(0x58E5CC, Add, 0xFFFFFE8D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE8D);
		SetMemory(0x58E5C8, Add, 0xFFFFFE8D);
		SetMemory(0x58E5C4, Add, 0x00000063);
		SetMemory(0x58E5CC, Add, 0x00000063);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000063);
		SetMemory(0x58E5C8, Add, 0x00000063);
		SetMemory(0x58E5C4, Add, 0x00000173);
		SetMemory(0x58E5CC, Add, 0x00000173);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000017F);
		SetMemory(0x58E5C8, Add, 0x0000017F);
		SetMemory(0x58E5C4, Add, 0x0000001A);
		SetMemory(0x58E5CC, Add, 0x0000001A);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCE);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCE);
		SetMemory(0x58E5C4, Add, 0xFFFFFE83);
		SetMemory(0x58E5CC, Add, 0xFFFFFE83);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE83);
		SetMemory(0x58E5C8, Add, 0xFFFFFE83);
		SetMemory(0x58E5C4, Add, 0x00000032);
		SetMemory(0x58E5CC, Add, 0x00000032);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000032);
		SetMemory(0x58E5C8, Add, 0x00000032);
		SetMemory(0x58E5C4, Add, 0x0000017D);
		SetMemory(0x58E5CC, Add, 0x0000017D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000B9);
		SetMemory(0x58E5C8, Add, 0x000000B9);
		SetMemory(0x58E5C4, Add, 0x00000151);
		SetMemory(0x58E5CC, Add, 0x00000151);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000002D);
		SetMemory(0x58E5C8, Add, 0x0000002D);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFE80);
		SetMemory(0x58E5CC, Add, 0xFFFFFE80);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD3);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD3);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE80);
		SetMemory(0x58E5C8, Add, 0xFFFFFE80);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD3);
		SetMemory(0x58E5C4, Add, 0x0000002D);
		SetMemory(0x58E5CC, Add, 0x0000002D);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000180);
		SetMemory(0x58E5CC, Add, 0x00000180);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000033);
		SetMemory(0x58E5C8, Add, 0x00000033);
		SetMemory(0x58E5C4, Add, 0x00000027);
		SetMemory(0x58E5CC, Add, 0x00000027);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF49);
		SetMemory(0x58E5C8, Add, 0xFFFFFF49);
		SetMemory(0x58E5C4, Add, 0x00000151);
		SetMemory(0x58E5CC, Add, 0x00000151);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000027);
		SetMemory(0x58E5C8, Add, 0x00000027);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCD);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCD);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000032);
		SetMemory(0x58E5C8, Add, 0x00000032);
		SetMemory(0x58E5C4, Add, 0xFFFFFE83);
		SetMemory(0x58E5CC, Add, 0xFFFFFE83);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 30, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCD);
		SetMemory(0x58E5C4, Add, 0xFFFFFFD9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFD9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE83);
		SetMemory(0x58E5C8, Add, 0xFFFFFE83);
		SetMemory(0x58E5C4, Add, 0xFFFFFFCE);
		SetMemory(0x58E5CC, Add, 0xFFFFFFCE);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 31, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFD9);
		SetMemory(0x58E5C4, Add, 0x00000033);
		SetMemory(0x58E5CC, Add, 0x00000033);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFCE);
		SetMemory(0x58E5C8, Add, 0xFFFFFFCE);
		SetMemory(0x58E5C4, Add, 0x0000017D);
		SetMemory(0x58E5CC, Add, 0x0000017D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 32, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000037);
		SetMemory(0x58E5C8, Add, 0x00000037);
		SetMemory(0x58E5C4, Add, 0x00000020);
		SetMemory(0x58E5CC, Add, 0x00000020);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE81);
		SetMemory(0x58E5C8, Add, 0xFFFFFE81);
		SetMemory(0x58E5C4, Add, 0x0000001C);
		SetMemory(0x58E5CC, Add, 0x0000001C);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 33, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000020);
		SetMemory(0x58E5C8, Add, 0x00000020);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC9);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC9);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000063);
		SetMemory(0x58E5C8, Add, 0x00000063);
		SetMemory(0x58E5C4, Add, 0xFFFFFE8D);
		SetMemory(0x58E5CC, Add, 0xFFFFFE8D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 34, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC9);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE8D);
		SetMemory(0x58E5C8, Add, 0xFFFFFE8D);
		SetMemory(0x58E5C4, Add, 0xFFFFFF9D);
		SetMemory(0x58E5CC, Add, 0xFFFFFF9D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 35, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE0);
		SetMemory(0x58E5C4, Add, 0x00000037);
		SetMemory(0x58E5CC, Add, 0x00000037);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF9D);
		SetMemory(0x58E5C8, Add, 0xFFFFFF9D);
		SetMemory(0x58E5C4, Add, 0x00000173);
		SetMemory(0x58E5CC, Add, 0x00000173);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 36, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003B);
		SetMemory(0x58E5C8, Add, 0x0000003B);
		SetMemory(0x58E5C4, Add, 0x00000018);
		SetMemory(0x58E5CC, Add, 0x00000018);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF1A);
		SetMemory(0x58E5C8, Add, 0xFFFFFF1A);
		SetMemory(0x58E5C4, Add, 0xFFFFFECD);
		SetMemory(0x58E5CC, Add, 0xFFFFFECD);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 37, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000018);
		SetMemory(0x58E5C8, Add, 0x00000018);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC5);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC5);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000093);
		SetMemory(0x58E5C8, Add, 0x00000093);
		SetMemory(0x58E5C4, Add, 0xFFFFFE9D);
		SetMemory(0x58E5CC, Add, 0xFFFFFE9D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 38, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC5);
		SetMemory(0x58E5C4, Add, 0xFFFFFFE8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFE8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFE9D);
		SetMemory(0x58E5C8, Add, 0xFFFFFE9D);
		SetMemory(0x58E5C4, Add, 0xFFFFFF6D);
		SetMemory(0x58E5CC, Add, 0xFFFFFF6D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 39, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFE8);
		SetMemory(0x58E5C4, Add, 0x0000003B);
		SetMemory(0x58E5CC, Add, 0x0000003B);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF6D);
		SetMemory(0x58E5C8, Add, 0xFFFFFF6D);
		SetMemory(0x58E5C4, Add, 0x00000163);
		SetMemory(0x58E5CC, Add, 0x00000163);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 40, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003E);
		SetMemory(0x58E5C8, Add, 0x0000003E);
		SetMemory(0x58E5C4, Add, 0x00000011);
		SetMemory(0x58E5CC, Add, 0x00000011);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000086);
		SetMemory(0x58E5C8, Add, 0x00000086);
		SetMemory(0x58E5C4, Add, 0xFFFFFE98);
		SetMemory(0x58E5CC, Add, 0xFFFFFE98);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 41, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000011);
		SetMemory(0x58E5C8, Add, 0x00000011);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC2);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC2);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000C0);
		SetMemory(0x58E5C8, Add, 0x000000C0);
		SetMemory(0x58E5C4, Add, 0xFFFFFEB3);
		SetMemory(0x58E5CC, Add, 0xFFFFFEB3);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 42, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC2);
		SetMemory(0x58E5C4, Add, 0xFFFFFFEF);
		SetMemory(0x58E5CC, Add, 0xFFFFFFEF);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEB3);
		SetMemory(0x58E5C8, Add, 0xFFFFFEB3);
		SetMemory(0x58E5C4, Add, 0xFFFFFF40);
		SetMemory(0x58E5CC, Add, 0xFFFFFF40);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 43, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C8, Add, 0xFFFFFFEF);
		SetMemory(0x58E5C4, Add, 0x0000003E);
		SetMemory(0x58E5CC, Add, 0x0000003E);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF40);
		SetMemory(0x58E5C8, Add, 0xFFFFFF40);
		SetMemory(0x58E5C4, Add, 0x0000014D);
		SetMemory(0x58E5CC, Add, 0x0000014D);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 44, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x0000003F);
		SetMemory(0x58E5C8, Add, 0x0000003F);
		SetMemory(0x58E5C4, Add, 0x00000008);
		SetMemory(0x58E5CC, Add, 0x00000008);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000177);
		SetMemory(0x58E5C8, Add, 0x00000177);
		SetMemory(0x58E5C4, Add, 0xFFFFFFAE);
		SetMemory(0x58E5CC, Add, 0xFFFFFFAE);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 45, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000008);
		SetMemory(0x58E5C8, Add, 0x00000008);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC1);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC1);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x000000EA);
		SetMemory(0x58E5C8, Add, 0x000000EA);
		SetMemory(0x58E5C4, Add, 0xFFFFFECF);
		SetMemory(0x58E5CC, Add, 0xFFFFFECF);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 46, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC1);
		SetMemory(0x58E5C4, Add, 0xFFFFFFF8);
		SetMemory(0x58E5CC, Add, 0xFFFFFFF8);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFECF);
		SetMemory(0x58E5C8, Add, 0xFFFFFECF);
		SetMemory(0x58E5C4, Add, 0xFFFFFF16);
		SetMemory(0x58E5CC, Add, 0xFFFFFF16);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 47, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C8, Add, 0xFFFFFFF8);
		SetMemory(0x58E5C4, Add, 0x0000003F);
		SetMemory(0x58E5CC, Add, 0x0000003F);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFF16);
		SetMemory(0x58E5C8, Add, 0xFFFFFF16);
		SetMemory(0x58E5C4, Add, 0x00000131);
		SetMemory(0x58E5CC, Add, 0x00000131);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 48, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000040);
		SetMemory(0x58E5C8, Add, 0x00000040);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 49, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0xFFFFFFC0);
		SetMemory(0x58E5CC, Add, 0xFFFFFFC0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000110);
		SetMemory(0x58E5C8, Add, 0x00000110);
		SetMemory(0x58E5C4, Add, 0xFFFFFEF0);
		SetMemory(0x58E5CC, Add, 0xFFFFFEF0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 50, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C8, Add, 0xFFFFFFC0);
		SetMemory(0x58E5C4, Add, 0x00000000);
		SetMemory(0x58E5CC, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C8, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C4, Add, 0xFFFFFEF0);
		SetMemory(0x58E5CC, Add, 0xFFFFFEF0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 51, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		SetMemory(0x58E5C0, Add, 0x00000000);
		SetMemory(0x58E5C8, Add, 0x00000000);
		SetMemory(0x58E5C4, Add, 0x00000040);
		SetMemory(0x58E5CC, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		MoveLocation("03.Maihime", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E5C0, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C8, Add, 0xFFFFFEF0);
		SetMemory(0x58E5C4, Add, 0x00000110);
		SetMemory(0x58E5CC, Add, 0x00000110);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "03.Maihime");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "03.Maihime_Bozo");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 52, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(3200);
		RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		SetSwitch("Recall - MaiHime", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("UiltimateSwitch", Clear);
	},
}
