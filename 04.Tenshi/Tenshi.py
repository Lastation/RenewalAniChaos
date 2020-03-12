Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 04.Tenshi
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3001, " * Dark Templar");
	},
	actions = {
		Comment("04.Tenshi");
		SetDeaths(AllPlayers, SetTo, 4, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 3000, " * Dark Templar");
		CreateUnit(1, " * Dark Templar", "[Select]Select Unit", CurrentPlayer);
		SetInvincibility(Enable, "Men", CurrentPlayer, "[Select]Select Unit");
		PreserveTrigger();
		RemoveUnitAt(All, " Struct. Spirit stone", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 4000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 1440, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 96, " `UniqueSkill");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 110, " `SkillStep");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 4000, " `SkillText");
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 120, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 4001, " `SkillText");
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 130, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 4002, " `SkillText");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 3, "Protoss Carrier", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 500, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, Subtract, 500, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		KillUnitAt(3, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 4003, " `SkillText");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 650, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Cleared);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 600, " Struct. Spirit stone");
		SetDeaths(CurrentPlayer, Subtract, 650, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 210, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("Recall - Tenshi", Set);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 650, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Set);
		Deaths(CurrentPlayer, Exactly, 0, " `UltimateCoolTime2");
	},
	actions = {
		Comment("Skill : Use Ultimate");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 800, Gas);
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

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 10);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Probe", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Probe", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Probe", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Probe", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Probe", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000060);
		SetMemory(0x58E610, Add, 0x00000060);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000060);
		SetMemory(0x58E610, Subtract, 0x00000060);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000060);
		SetMemory(0x58E61C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Creep. Licht", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000060);
		SetMemory(0x58E610, Add, 0x00000060);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000060);
		SetMemory(0x58E610, Subtract, 0x00000060);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000060);
		SetMemory(0x58E610, Subtract, 0x00000060);
		SetMemory(0x58E614, Subtract, 0x00000060);
		SetMemory(0x58E61C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000060);
		SetMemory(0x58E610, Add, 0x00000060);
		SetMemory(0x58E614, Subtract, 0x00000060);
		SetMemory(0x58E61C, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, " Creep. Licht", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(1300);
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(130);
		KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
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
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0xFFFFFFA0);
		SetMemory(0x58E61C, Add, 0xFFFFFFA0);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0xFFFFFFA0);
		SetMemory(0x58E61C, Add, 0xFFFFFFA0);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000030);
		SetMemory(0x58E618, Add, 0x00000030);
		SetMemory(0x58E614, Add, 0x00000054);
		SetMemory(0x58E61C, Add, 0x00000054);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000030);
		SetMemory(0x58E618, Add, 0x00000030);
		SetMemory(0x58E614, Add, 0x00000054);
		SetMemory(0x58E61C, Add, 0x00000054);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFD0);
		SetMemory(0x58E618, Add, 0xFFFFFFD0);
		SetMemory(0x58E614, Add, 0xFFFFFFAC);
		SetMemory(0x58E61C, Add, 0xFFFFFFAC);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFD0);
		SetMemory(0x58E618, Add, 0xFFFFFFD0);
		SetMemory(0x58E614, Add, 0xFFFFFFAC);
		SetMemory(0x58E61C, Add, 0xFFFFFFAC);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000054);
		SetMemory(0x58E618, Add, 0x00000054);
		SetMemory(0x58E614, Add, 0x00000030);
		SetMemory(0x58E61C, Add, 0x00000030);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000054);
		SetMemory(0x58E618, Add, 0x00000054);
		SetMemory(0x58E614, Add, 0x00000030);
		SetMemory(0x58E61C, Add, 0x00000030);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFAC);
		SetMemory(0x58E618, Add, 0xFFFFFFAC);
		SetMemory(0x58E614, Add, 0xFFFFFFD0);
		SetMemory(0x58E61C, Add, 0xFFFFFFD0);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFAC);
		SetMemory(0x58E618, Add, 0xFFFFFFAC);
		SetMemory(0x58E614, Add, 0xFFFFFFD0);
		SetMemory(0x58E61C, Add, 0xFFFFFFD0);
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000060);
		SetMemory(0x58E618, Add, 0x00000060);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000060);
		SetMemory(0x58E618, Add, 0x00000060);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFA0);
		SetMemory(0x58E618, Add, 0xFFFFFFA0);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFA0);
		SetMemory(0x58E618, Add, 0xFFFFFFA0);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000054);
		SetMemory(0x58E618, Add, 0x00000054);
		SetMemory(0x58E614, Add, 0xFFFFFFD0);
		SetMemory(0x58E61C, Add, 0xFFFFFFD0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000054);
		SetMemory(0x58E618, Add, 0x00000054);
		SetMemory(0x58E614, Add, 0xFFFFFFD0);
		SetMemory(0x58E61C, Add, 0xFFFFFFD0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFAC);
		SetMemory(0x58E618, Add, 0xFFFFFFAC);
		SetMemory(0x58E614, Add, 0x00000030);
		SetMemory(0x58E61C, Add, 0x00000030);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFAC);
		SetMemory(0x58E618, Add, 0xFFFFFFAC);
		SetMemory(0x58E614, Add, 0x00000030);
		SetMemory(0x58E61C, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000030);
		SetMemory(0x58E618, Add, 0x00000030);
		SetMemory(0x58E614, Add, 0xFFFFFFAC);
		SetMemory(0x58E61C, Add, 0xFFFFFFAC);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000030);
		SetMemory(0x58E618, Add, 0x00000030);
		SetMemory(0x58E614, Add, 0xFFFFFFAC);
		SetMemory(0x58E61C, Add, 0xFFFFFFAC);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFD0);
		SetMemory(0x58E618, Add, 0xFFFFFFD0);
		SetMemory(0x58E614, Add, 0x00000054);
		SetMemory(0x58E61C, Add, 0x00000054);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0xFFFFFFD0);
		SetMemory(0x58E618, Add, 0xFFFFFFD0);
		SetMemory(0x58E614, Add, 0x00000054);
		SetMemory(0x58E61C, Add, 0x00000054);
		MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0xFFFFFFA0);
		SetMemory(0x58E61C, Add, 0xFFFFFFA0);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0xFFFFFFA0);
		SetMemory(0x58E61C, Add, 0xFFFFFFA0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000060);
		SetMemory(0x58E61C, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(1000);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		Wait(400);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000080);
		SetMemory(0x58E610, Add, 0x00000080);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x000000A0);
		SetMemory(0x58E61C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Subtract, 0x00000020);
		SetMemory(0x58E61C, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000A0);
		SetMemory(0x58E610, Subtract, 0x000000A0);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000020);
		SetMemory(0x58E610, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x000000A0);
		SetMemory(0x58E61C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E614, Add, 0x00000020);
		SetMemory(0x58E61C, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000A0);
		SetMemory(0x58E610, Add, 0x000000A0);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000020);
		SetMemory(0x58E610, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(100);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(500);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
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
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000100);
		SetMemory(0x58E61C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000100);
		SetMemory(0x58E61C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000100);
		SetMemory(0x58E61C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000100);
		SetMemory(0x58E61C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000100);
		SetMemory(0x58E61C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000100);
		SetMemory(0x58E61C, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000100);
		SetMemory(0x58E61C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000100);
		SetMemory(0x58E61C, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Bengalaas (Jungle)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Rhynadon (Badlands)", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(30);
		RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000100);
		SetMemory(0x58E610, Subtract, 0x00000100);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x000000C0);
		SetMemory(0x58E610, Subtract, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000080);
		SetMemory(0x58E610, Subtract, 0x00000080);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Subtract, 0x00000000);
		SetMemory(0x58E610, Subtract, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000100);
		SetMemory(0x58E61C, Add, 0x00000100);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Add, 0x00000040);
		SetMemory(0x58E610, Add, 0x00000040);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		ModifyUnitHangarCount(3, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");
		Wait(2000);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		RemoveUnitAt(All, " Struct. Spirit stone", "Anywhere", CurrentPlayer);
		CreateUnit(1, " Struct. Spirit stone", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, " * Dark Templar", CurrentPlayer, "Anywhere", "[Line]Center_Line");
		MoveUnit(1, " Struct. Spirit stone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, " * Dark Templar", CurrentPlayer, "Anywhere", "04.Tenshi_Bozo");
		SetDeaths(CurrentPlayer, SetTo, 600, " Struct. Spirit stone");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, " Struct. Spirit stone", "[Skill]Unit_Wait_ALL");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		RemoveUnitAt(All, " Struct. Spirit stone", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 500, Gas);
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetAllianceStatus(P7, Ally);
		SetAllianceStatus(P8, Ally);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 4000, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillCount");
		Wait(650);
		MoveLocation("04.Tenshi_Bozo", " Struct. Spirit stone", CurrentPlayer, "Anywhere");
		KillUnitAt(1, " Struct. Spirit stone", "Anywhere", CurrentPlayer);
		KillUnitAt(1, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		SetInvincibility(Enable, " * Dark Templar", CurrentPlayer, "Anywhere");
		Wait(0);
		MoveUnit(All, " * Dark Templar", CurrentPlayer, "Anywhere", "04.Tenshi_Bozo");
		CenterView("04.Tenshi_Bozo");
		SetDeaths(AllPlayers, SetTo, 4001, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(80);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x000000C0);
		SetMemory(0x58E61C, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000080);
		SetMemory(0x58E61C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000040);
		SetMemory(0x58E61C, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Subtract, 0x00000000);
		SetMemory(0x58E61C, Subtract, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(80);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x000000C0);
		SetMemory(0x58E610, Add, 0x000000C0);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(80);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x000000C0);
		SetMemory(0x58E61C, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000080);
		SetMemory(0x58E61C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000040);
		SetMemory(0x58E61C, Add, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E618, Add, 0x00000000);
		SetMemory(0x58E610, Add, 0x00000000);
		SetMemory(0x58E614, Add, 0x00000000);
		SetMemory(0x58E61C, Add, 0x00000000);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		SetMemory(0x58E618, Subtract, 0x00000040);
		SetMemory(0x58E610, Subtract, 0x00000040);
		MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi");
		Wait(80);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, AtMost, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillCount");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetAllianceStatus(P7, Enemy);
		SetAllianceStatus(P8, Enemy);
		SetInvincibility(Disable, " * Dark Templar", CurrentPlayer, "Anywhere");
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
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(1, "Target", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 1);
		KillUnit("Protoss Observer", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		GiveUnits(All, "80 + 1n Artanis", P7, "Anywhere", P12);
		GiveUnits(All, "80 + 1n Tom Kazansky", P7, "Anywhere", P12);
		GiveUnits(All, "100 + 1n Hyperion", P7, "Anywhere", P12);
		GiveUnits(All, "130 + 1n Arbiter", P7, "Anywhere", P12);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		GiveUnits(All, "80 + 1n Artanis", P8, "Anywhere", P12);
		GiveUnits(All, "80 + 1n Tom Kazansky", P8, "Anywhere", P12);
		GiveUnits(All, "100 + 1n Hyperion", P8, "Anywhere", P12);
		GiveUnits(All, "130 + 1n Arbiter", P8, "Anywhere", P12);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetSwitch("JunkYardDog - Tenshi", Set);
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillCount");
		SetDeaths(AllPlayers, SetTo, 4010, " `SkillText_Uiltimate");
		SetSwitch("ComputerAlliy", Set);
		Wait(2200);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		Wait(2500);
		SetDeaths(CurrentPlayer, SetTo, 999, " `SkillCount");
		SetSwitch("ComputerAlliy", Clear);
		Wait(300);
		SetDeaths(AllPlayers, SetTo, 4011, " `SkillText_Uiltimate");
		GiveUnits(All, "80 + 1n Artanis", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Tom Kazansky", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "130 + 1n Arbiter", P12, "Anywhere", CurrentPlayer);
		Wait(0);
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Wait(750);
		SetDeaths(AllPlayers, SetTo, 4012, " `SkillText_Uiltimate");
		SetSwitch("JunkYardDog - Tenshi", Clear);
		SetSwitch("Recall - Tenshi", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 3, " `SkillCount");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Artanis", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Kakaru (Twilight)", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", P7);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "80 + 1n Artanis", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_6", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(2, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Artanis", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "Kakaru (Twilight)", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", P8);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "100 + 1n Hyperion", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "130 + 1n Arbiter", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "100 + 1n Hyperion", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "130 + 1n Arbiter", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P7);
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P7);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "100 + 1n Hyperion", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "130 + 1n Arbiter", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "04.Tenshi_Bozo");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi_Bozo");
		RemoveUnitAt(All, "100 + 1n Hyperion", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "130 + 1n Arbiter", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		GiveUnits(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", P8);
		GiveUnits(All, "130 + 1n Arbiter", CurrentPlayer, "Anywhere", P8);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("04.Tenshi", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveLocation("04.Tenshi", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
		RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "04.Tenshi");
		Order("80 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Goliath", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Tank", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		RemoveUnitAt(All, "80 + 1n Vulture", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Bring(CurrentPlayer, Exactly, 0, "Kakaru (Twilight)", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Ultimate");
		Order("80 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("130 + 1n Arbiter", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "04.Tenshi_Bozo");
		RemoveUnitAt(All, "Any unit", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		Wait(3000);
		KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Clear);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		PreserveTrigger();
	},
}