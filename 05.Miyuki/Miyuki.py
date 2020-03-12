Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- 05.Miyuki
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2001, " * Dark Templar");
	},
	actions = {
		Comment("05.Miyuki");
		SetDeaths(AllPlayers, SetTo, 5, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(CurrentPlayer, SetTo, 2000, " * Dark Templar");
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

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtLeast, 25);
	},
	actions = {
		Comment("Skill : Use Skill");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 5000, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillStep");
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(200);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(AllPlayers, SetTo, 5001, " `SkillText_Unique");
		SetDeaths(CurrentPlayer, SetTo, 1080, " `UniqueCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 60, " `UniqueSkill");
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		SetDeaths(AllPlayers, SetTo, 5400, " `SkillText");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		SetDeaths(AllPlayers, SetTo, 5300, " `SkillText");
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 310, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 5000, " `SkillText");
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 5100, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 330, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 5200, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
		SetSwitch("UiltimateSwitch", Set);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, AtLeast, 250, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Set);
	},
	actions = {
		Comment("Skill : Use Ultimate");
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 800, Gas);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
		MoveLocation("05.Miyuki_FindForce", " * Dark Templar", CurrentPlayer, "Anywhere");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(Foes, Exactly, 2000, " * Dark Templar");
		Deaths(Foes, AtLeast, 1, " `UniqueSkill");
		Bring(CurrentPlayer, AtLeast, 1, "Men", "05.Miyuki_FindForce");
	},
	actions = {
		Comment("Skill : Unique");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SystemDebuff_Slow");
		RemoveUnit("Protoss Observer", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(10, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(5, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : S");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : C
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
	},
	actions = {
		Comment("Skill : C");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000012);
		SetMemory(0x58E624, Add, 0x00000012);
		SetMemory(0x58E628, Add, 0x00000012);
		SetMemory(0x58E630, Add, 0x00000012);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000012);
		SetMemory(0x58E624, Subtract, 0x00000012);
		SetMemory(0x58E628, Add, 0x00000012);
		SetMemory(0x58E630, Add, 0x00000012);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000012);
		SetMemory(0x58E624, Subtract, 0x00000012);
		SetMemory(0x58E628, Subtract, 0x00000012);
		SetMemory(0x58E630, Subtract, 0x00000012);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000012);
		SetMemory(0x58E624, Add, 0x00000012);
		SetMemory(0x58E628, Subtract, 0x00000012);
		SetMemory(0x58E630, Subtract, 0x00000012);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000036);
		SetMemory(0x58E624, Add, 0x00000036);
		SetMemory(0x58E628, Add, 0x00000036);
		SetMemory(0x58E630, Add, 0x00000036);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000036);
		SetMemory(0x58E624, Subtract, 0x00000036);
		SetMemory(0x58E628, Add, 0x00000036);
		SetMemory(0x58E630, Add, 0x00000036);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000036);
		SetMemory(0x58E624, Subtract, 0x00000036);
		SetMemory(0x58E628, Subtract, 0x00000036);
		SetMemory(0x58E630, Subtract, 0x00000036);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000036);
		SetMemory(0x58E624, Add, 0x00000036);
		SetMemory(0x58E628, Subtract, 0x00000036);
		SetMemory(0x58E630, Subtract, 0x00000036);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000005A);
		SetMemory(0x58E624, Add, 0x0000005A);
		SetMemory(0x58E628, Add, 0x0000005A);
		SetMemory(0x58E630, Add, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000005A);
		SetMemory(0x58E624, Subtract, 0x0000005A);
		SetMemory(0x58E628, Add, 0x0000005A);
		SetMemory(0x58E630, Add, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000005A);
		SetMemory(0x58E624, Subtract, 0x0000005A);
		SetMemory(0x58E628, Subtract, 0x0000005A);
		SetMemory(0x58E630, Subtract, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000005A);
		SetMemory(0x58E624, Add, 0x0000005A);
		SetMemory(0x58E628, Subtract, 0x0000005A);
		SetMemory(0x58E630, Subtract, 0x0000005A);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000007E);
		SetMemory(0x58E624, Add, 0x0000007E);
		SetMemory(0x58E628, Add, 0x0000007E);
		SetMemory(0x58E630, Add, 0x0000007E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000007E);
		SetMemory(0x58E624, Subtract, 0x0000007E);
		SetMemory(0x58E628, Add, 0x0000007E);
		SetMemory(0x58E630, Add, 0x0000007E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000007E);
		SetMemory(0x58E624, Subtract, 0x0000007E);
		SetMemory(0x58E628, Subtract, 0x0000007E);
		SetMemory(0x58E630, Subtract, 0x0000007E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000007E);
		SetMemory(0x58E624, Add, 0x0000007E);
		SetMemory(0x58E628, Subtract, 0x0000007E);
		SetMemory(0x58E630, Subtract, 0x0000007E);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000078);
		SetMemory(0x58E624, Add, 0x00000078);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000078);
		SetMemory(0x58E630, Add, 0x00000078);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000078);
		SetMemory(0x58E624, Subtract, 0x00000078);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000078);
		SetMemory(0x58E630, Subtract, 0x00000078);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A8);
		SetMemory(0x58E624, Add, 0x000000A8);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000A8);
		SetMemory(0x58E630, Add, 0x000000A8);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A8);
		SetMemory(0x58E624, Subtract, 0x000000A8);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000A8);
		SetMemory(0x58E630, Subtract, 0x000000A8);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFFB0);
		SetMemory(0x58E630, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB0);
		SetMemory(0x58E624, Add, 0xFFFFFFB0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001F);
		SetMemory(0x58E624, Add, 0x0000001F);
		SetMemory(0x58E628, Add, 0x0000004A);
		SetMemory(0x58E630, Add, 0x0000004A);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004A);
		SetMemory(0x58E624, Add, 0x0000004A);
		SetMemory(0x58E628, Add, 0xFFFFFFE1);
		SetMemory(0x58E630, Add, 0xFFFFFFE1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE1);
		SetMemory(0x58E624, Add, 0xFFFFFFE1);
		SetMemory(0x58E628, Add, 0xFFFFFFB6);
		SetMemory(0x58E630, Add, 0xFFFFFFB6);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB6);
		SetMemory(0x58E624, Add, 0xFFFFFFB6);
		SetMemory(0x58E628, Add, 0x0000001F);
		SetMemory(0x58E630, Add, 0x0000001F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004A);
		SetMemory(0x58E624, Add, 0x0000004A);
		SetMemory(0x58E628, Add, 0x0000001F);
		SetMemory(0x58E630, Add, 0x0000001F);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001F);
		SetMemory(0x58E624, Add, 0x0000001F);
		SetMemory(0x58E628, Add, 0xFFFFFFB6);
		SetMemory(0x58E630, Add, 0xFFFFFFB6);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB6);
		SetMemory(0x58E624, Add, 0xFFFFFFB6);
		SetMemory(0x58E628, Add, 0xFFFFFFE1);
		SetMemory(0x58E630, Add, 0xFFFFFFE1);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE1);
		SetMemory(0x58E624, Add, 0xFFFFFFE1);
		SetMemory(0x58E628, Add, 0x0000004A);
		SetMemory(0x58E630, Add, 0x0000004A);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFFB0);
		SetMemory(0x58E630, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB0);
		SetMemory(0x58E624, Add, 0xFFFFFFB0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004A);
		SetMemory(0x58E624, Add, 0x0000004A);
		SetMemory(0x58E628, Add, 0xFFFFFFE1);
		SetMemory(0x58E630, Add, 0xFFFFFFE1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE1);
		SetMemory(0x58E624, Add, 0xFFFFFFE1);
		SetMemory(0x58E628, Add, 0xFFFFFFB6);
		SetMemory(0x58E630, Add, 0xFFFFFFB6);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB6);
		SetMemory(0x58E624, Add, 0xFFFFFFB6);
		SetMemory(0x58E628, Add, 0x0000001F);
		SetMemory(0x58E630, Add, 0x0000001F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001F);
		SetMemory(0x58E624, Add, 0x0000001F);
		SetMemory(0x58E628, Add, 0x0000004A);
		SetMemory(0x58E630, Add, 0x0000004A);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "40 + 1n Zealot", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001F);
		SetMemory(0x58E624, Add, 0x0000001F);
		SetMemory(0x58E628, Add, 0xFFFFFFB6);
		SetMemory(0x58E630, Add, 0xFFFFFFB6);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB6);
		SetMemory(0x58E624, Add, 0xFFFFFFB6);
		SetMemory(0x58E628, Add, 0xFFFFFFE1);
		SetMemory(0x58E630, Add, 0xFFFFFFE1);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE1);
		SetMemory(0x58E624, Add, 0xFFFFFFE1);
		SetMemory(0x58E628, Add, 0x0000004A);
		SetMemory(0x58E630, Add, 0x0000004A);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004A);
		SetMemory(0x58E624, Add, 0x0000004A);
		SetMemory(0x58E628, Add, 0x0000001F);
		SetMemory(0x58E630, Add, 0x0000001F);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Wait(0);
		RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
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

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		Wait(130);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		Wait(1000);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(230);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(800);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		MoveUnit(All, "40 + 1n Ghost", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, " Creep. Dunkelheit", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "40 + 1n Wraith", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
		MoveUnit(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "40 + 1n Zealot", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000180);
		SetMemory(0x58E624, Add, 0x00000180);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000180);
		SetMemory(0x58E630, Add, 0x00000180);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000180);
		SetMemory(0x58E624, Subtract, 0x00000180);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000180);
		SetMemory(0x58E630, Subtract, 0x00000180);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(32, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(8, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("60 + 1n Siege", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("60 + 1n Siege", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("60 + 1n Siege", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000180);
		SetMemory(0x58E630, Add, 0x00000180);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000180);
		SetMemory(0x58E624, Subtract, 0x00000180);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000180);
		SetMemory(0x58E630, Subtract, 0x00000180);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000180);
		SetMemory(0x58E624, Add, 0x00000180);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);
		CreateUnit(8, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(8, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		Wait(1000);
		SetDeaths(AllPlayers, Add, 5301, " `SkillText");
		Wait(2600);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 1);
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000012);
		SetMemory(0x58E624, Add, 0x00000012);
		SetMemory(0x58E628, Add, 0x00000012);
		SetMemory(0x58E630, Add, 0x00000012);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000012);
		SetMemory(0x58E624, Subtract, 0x00000012);
		SetMemory(0x58E628, Add, 0x00000012);
		SetMemory(0x58E630, Add, 0x00000012);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000012);
		SetMemory(0x58E624, Subtract, 0x00000012);
		SetMemory(0x58E628, Subtract, 0x00000012);
		SetMemory(0x58E630, Subtract, 0x00000012);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000012);
		SetMemory(0x58E624, Add, 0x00000012);
		SetMemory(0x58E628, Subtract, 0x00000012);
		SetMemory(0x58E630, Subtract, 0x00000012);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000018);
		SetMemory(0x58E624, Add, 0x00000018);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000018);
		SetMemory(0x58E630, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000018);
		SetMemory(0x58E624, Subtract, 0x00000018);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000018);
		SetMemory(0x58E630, Subtract, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000024);
		SetMemory(0x58E624, Add, 0x00000024);
		SetMemory(0x58E628, Add, 0x00000024);
		SetMemory(0x58E630, Add, 0x00000024);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000024);
		SetMemory(0x58E624, Subtract, 0x00000024);
		SetMemory(0x58E628, Add, 0x00000024);
		SetMemory(0x58E630, Add, 0x00000024);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000024);
		SetMemory(0x58E624, Subtract, 0x00000024);
		SetMemory(0x58E628, Subtract, 0x00000024);
		SetMemory(0x58E630, Subtract, 0x00000024);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000024);
		SetMemory(0x58E624, Add, 0x00000024);
		SetMemory(0x58E628, Subtract, 0x00000024);
		SetMemory(0x58E630, Subtract, 0x00000024);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000036);
		SetMemory(0x58E624, Add, 0x00000036);
		SetMemory(0x58E628, Add, 0x00000036);
		SetMemory(0x58E630, Add, 0x00000036);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000036);
		SetMemory(0x58E624, Subtract, 0x00000036);
		SetMemory(0x58E628, Add, 0x00000036);
		SetMemory(0x58E630, Add, 0x00000036);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000036);
		SetMemory(0x58E624, Subtract, 0x00000036);
		SetMemory(0x58E628, Subtract, 0x00000036);
		SetMemory(0x58E630, Subtract, 0x00000036);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000036);
		SetMemory(0x58E624, Add, 0x00000036);
		SetMemory(0x58E628, Subtract, 0x00000036);
		SetMemory(0x58E630, Subtract, 0x00000036);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Add, 0x00000048);
		SetMemory(0x58E630, Add, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000048);
		SetMemory(0x58E624, Subtract, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000048);
		SetMemory(0x58E624, Add, 0x00000048);
		SetMemory(0x58E628, Subtract, 0x00000048);
		SetMemory(0x58E630, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000005A);
		SetMemory(0x58E624, Add, 0x0000005A);
		SetMemory(0x58E628, Add, 0x0000005A);
		SetMemory(0x58E630, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000005A);
		SetMemory(0x58E624, Subtract, 0x0000005A);
		SetMemory(0x58E628, Add, 0x0000005A);
		SetMemory(0x58E630, Add, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000005A);
		SetMemory(0x58E624, Subtract, 0x0000005A);
		SetMemory(0x58E628, Subtract, 0x0000005A);
		SetMemory(0x58E630, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000005A);
		SetMemory(0x58E624, Add, 0x0000005A);
		SetMemory(0x58E628, Subtract, 0x0000005A);
		SetMemory(0x58E630, Subtract, 0x0000005A);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000078);
		SetMemory(0x58E624, Add, 0x00000078);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000078);
		SetMemory(0x58E630, Add, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000078);
		SetMemory(0x58E624, Subtract, 0x00000078);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000078);
		SetMemory(0x58E630, Subtract, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000006C);
		SetMemory(0x58E624, Subtract, 0x0000006C);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000006C);
		SetMemory(0x58E624, Subtract, 0x0000006C);
		SetMemory(0x58E628, Subtract, 0x0000006C);
		SetMemory(0x58E630, Subtract, 0x0000006C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Subtract, 0x0000006C);
		SetMemory(0x58E630, Subtract, 0x0000006C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000007E);
		SetMemory(0x58E624, Add, 0x0000007E);
		SetMemory(0x58E628, Add, 0x0000007E);
		SetMemory(0x58E630, Add, 0x0000007E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000007E);
		SetMemory(0x58E624, Subtract, 0x0000007E);
		SetMemory(0x58E628, Add, 0x0000007E);
		SetMemory(0x58E630, Add, 0x0000007E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x0000007E);
		SetMemory(0x58E624, Subtract, 0x0000007E);
		SetMemory(0x58E628, Subtract, 0x0000007E);
		SetMemory(0x58E630, Subtract, 0x0000007E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000007E);
		SetMemory(0x58E624, Add, 0x0000007E);
		SetMemory(0x58E628, Subtract, 0x0000007E);
		SetMemory(0x58E630, Subtract, 0x0000007E);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A8);
		SetMemory(0x58E624, Add, 0x000000A8);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000A8);
		SetMemory(0x58E630, Add, 0x000000A8);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A8);
		SetMemory(0x58E624, Subtract, 0x000000A8);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000A8);
		SetMemory(0x58E630, Subtract, 0x000000A8);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A2);
		SetMemory(0x58E624, Add, 0x000000A2);
		SetMemory(0x58E628, Add, 0x000000A2);
		SetMemory(0x58E630, Add, 0x000000A2);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A2);
		SetMemory(0x58E624, Subtract, 0x000000A2);
		SetMemory(0x58E628, Add, 0x000000A2);
		SetMemory(0x58E630, Add, 0x000000A2);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A2);
		SetMemory(0x58E624, Subtract, 0x000000A2);
		SetMemory(0x58E628, Subtract, 0x000000A2);
		SetMemory(0x58E630, Subtract, 0x000000A2);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A2);
		SetMemory(0x58E624, Add, 0x000000A2);
		SetMemory(0x58E628, Subtract, 0x000000A2);
		SetMemory(0x58E630, Subtract, 0x000000A2);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000D8);
		SetMemory(0x58E624, Add, 0x000000D8);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000D8);
		SetMemory(0x58E630, Add, 0x000000D8);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000D8);
		SetMemory(0x58E624, Subtract, 0x000000D8);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000D8);
		SetMemory(0x58E630, Subtract, 0x000000D8);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000084);
		SetMemory(0x58E624, Add, 0x00000084);
		SetMemory(0x58E628, Add, 0x00000084);
		SetMemory(0x58E630, Add, 0x00000084);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000084);
		SetMemory(0x58E624, Subtract, 0x00000084);
		SetMemory(0x58E628, Add, 0x00000084);
		SetMemory(0x58E630, Add, 0x00000084);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000084);
		SetMemory(0x58E624, Subtract, 0x00000084);
		SetMemory(0x58E628, Subtract, 0x00000084);
		SetMemory(0x58E630, Subtract, 0x00000084);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000084);
		SetMemory(0x58E624, Add, 0x00000084);
		SetMemory(0x58E628, Subtract, 0x00000084);
		SetMemory(0x58E630, Subtract, 0x00000084);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "Protoss Dark Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(1300);
		SetDeaths(AllPlayers, SetTo, 5001, " `SkillText");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFF60);
		SetMemory(0x58E630, Add, 0xFFFFFF60);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF60);
		SetMemory(0x58E624, Add, 0xFFFFFF60);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Add, 0x00000090);
		SetMemory(0x58E630, Add, 0x00000090);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000090);
		SetMemory(0x58E624, Subtract, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000090);
		SetMemory(0x58E624, Add, 0x00000090);
		SetMemory(0x58E628, Subtract, 0x00000090);
		SetMemory(0x58E630, Subtract, 0x00000090);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFFA0);
		SetMemory(0x58E630, Add, 0xFFFFFFA0);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFA0);
		SetMemory(0x58E624, Add, 0xFFFFFFA0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Ghost", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000054);
		SetMemory(0x58E624, Add, 0x00000054);
		SetMemory(0x58E628, Add, 0x00000054);
		SetMemory(0x58E630, Add, 0x00000054);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000054);
		SetMemory(0x58E624, Subtract, 0x00000054);
		SetMemory(0x58E628, Add, 0x00000054);
		SetMemory(0x58E630, Add, 0x00000054);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000054);
		SetMemory(0x58E624, Subtract, 0x00000054);
		SetMemory(0x58E628, Subtract, 0x00000054);
		SetMemory(0x58E630, Subtract, 0x00000054);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000054);
		SetMemory(0x58E624, Add, 0x00000054);
		SetMemory(0x58E628, Subtract, 0x00000054);
		SetMemory(0x58E630, Subtract, 0x00000054);
		MoveUnit(1, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(800);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFFB0);
		SetMemory(0x58E630, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB0);
		SetMemory(0x58E624, Add, 0xFFFFFFB0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004F);
		SetMemory(0x58E624, Add, 0x0000004F);
		SetMemory(0x58E628, Add, 0x0000004F);
		SetMemory(0x58E630, Add, 0x0000004F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004F);
		SetMemory(0x58E624, Add, 0x0000004F);
		SetMemory(0x58E628, Add, 0xFFFFFFB1);
		SetMemory(0x58E630, Add, 0xFFFFFFB1);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB1);
		SetMemory(0x58E624, Add, 0xFFFFFFB1);
		SetMemory(0x58E628, Add, 0xFFFFFFB1);
		SetMemory(0x58E630, Add, 0xFFFFFFB1);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB1);
		SetMemory(0x58E624, Add, 0xFFFFFFB1);
		SetMemory(0x58E628, Add, 0x0000004F);
		SetMemory(0x58E630, Add, 0x0000004F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000015);
		SetMemory(0x58E624, Add, 0x00000015);
		SetMemory(0x58E628, Add, 0x0000004D);
		SetMemory(0x58E630, Add, 0x0000004D);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004D);
		SetMemory(0x58E624, Add, 0x0000004D);
		SetMemory(0x58E628, Add, 0xFFFFFFEB);
		SetMemory(0x58E630, Add, 0xFFFFFFEB);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFEB);
		SetMemory(0x58E624, Add, 0xFFFFFFEB);
		SetMemory(0x58E628, Add, 0xFFFFFFB3);
		SetMemory(0x58E630, Add, 0xFFFFFFB3);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB3);
		SetMemory(0x58E624, Add, 0xFFFFFFB3);
		SetMemory(0x58E628, Add, 0x00000015);
		SetMemory(0x58E630, Add, 0x00000015);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000061);
		SetMemory(0x58E624, Add, 0x00000061);
		SetMemory(0x58E628, Add, 0x00000038);
		SetMemory(0x58E630, Add, 0x00000038);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000038);
		SetMemory(0x58E624, Add, 0x00000038);
		SetMemory(0x58E628, Add, 0xFFFFFF9F);
		SetMemory(0x58E630, Add, 0xFFFFFF9F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF9F);
		SetMemory(0x58E624, Add, 0xFFFFFF9F);
		SetMemory(0x58E628, Add, 0xFFFFFFC8);
		SetMemory(0x58E630, Add, 0xFFFFFFC8);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC8);
		SetMemory(0x58E624, Add, 0xFFFFFFC8);
		SetMemory(0x58E628, Add, 0x00000061);
		SetMemory(0x58E630, Add, 0x00000061);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000028);
		SetMemory(0x58E624, Add, 0x00000028);
		SetMemory(0x58E628, Add, 0x00000045);
		SetMemory(0x58E630, Add, 0x00000045);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000045);
		SetMemory(0x58E624, Add, 0x00000045);
		SetMemory(0x58E628, Add, 0xFFFFFFD8);
		SetMemory(0x58E630, Add, 0xFFFFFFD8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFD8);
		SetMemory(0x58E624, Add, 0xFFFFFFD8);
		SetMemory(0x58E628, Add, 0xFFFFFFBB);
		SetMemory(0x58E630, Add, 0xFFFFFFBB);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFBB);
		SetMemory(0x58E624, Add, 0xFFFFFFBB);
		SetMemory(0x58E628, Add, 0x00000028);
		SetMemory(0x58E630, Add, 0x00000028);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Add, 0x0000001D);
		SetMemory(0x58E630, Add, 0x0000001D);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001D);
		SetMemory(0x58E624, Add, 0x0000001D);
		SetMemory(0x58E628, Add, 0xFFFFFF94);
		SetMemory(0x58E630, Add, 0xFFFFFF94);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF94);
		SetMemory(0x58E624, Add, 0xFFFFFF94);
		SetMemory(0x58E628, Add, 0xFFFFFFE3);
		SetMemory(0x58E630, Add, 0xFFFFFFE3);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE3);
		SetMemory(0x58E624, Add, 0xFFFFFFE3);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000070);
		SetMemory(0x58E624, Add, 0x00000070);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFF90);
		SetMemory(0x58E630, Add, 0xFFFFFF90);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF90);
		SetMemory(0x58E624, Add, 0xFFFFFF90);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000070);
		SetMemory(0x58E630, Add, 0x00000070);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000045);
		SetMemory(0x58E624, Add, 0x00000045);
		SetMemory(0x58E628, Add, 0x00000028);
		SetMemory(0x58E630, Add, 0x00000028);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000028);
		SetMemory(0x58E624, Add, 0x00000028);
		SetMemory(0x58E628, Add, 0xFFFFFFBB);
		SetMemory(0x58E630, Add, 0xFFFFFFBB);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFBB);
		SetMemory(0x58E624, Add, 0xFFFFFFBB);
		SetMemory(0x58E628, Add, 0xFFFFFFD8);
		SetMemory(0x58E630, Add, 0xFFFFFFD8);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFD8);
		SetMemory(0x58E624, Add, 0xFFFFFFD8);
		SetMemory(0x58E628, Add, 0x00000045);
		SetMemory(0x58E630, Add, 0x00000045);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Add, 0xFFFFFFE3);
		SetMemory(0x58E630, Add, 0xFFFFFFE3);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE3);
		SetMemory(0x58E624, Add, 0xFFFFFFE3);
		SetMemory(0x58E628, Add, 0xFFFFFF94);
		SetMemory(0x58E630, Add, 0xFFFFFF94);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF94);
		SetMemory(0x58E624, Add, 0xFFFFFF94);
		SetMemory(0x58E628, Add, 0x0000001D);
		SetMemory(0x58E630, Add, 0x0000001D);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001D);
		SetMemory(0x58E624, Add, 0x0000001D);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004D);
		SetMemory(0x58E624, Add, 0x0000004D);
		SetMemory(0x58E628, Add, 0x00000015);
		SetMemory(0x58E630, Add, 0x00000015);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000015);
		SetMemory(0x58E624, Add, 0x00000015);
		SetMemory(0x58E628, Add, 0xFFFFFFB3);
		SetMemory(0x58E630, Add, 0xFFFFFFB3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB3);
		SetMemory(0x58E624, Add, 0xFFFFFFB3);
		SetMemory(0x58E628, Add, 0xFFFFFFEB);
		SetMemory(0x58E630, Add, 0xFFFFFFEB);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFEB);
		SetMemory(0x58E624, Add, 0xFFFFFFEB);
		SetMemory(0x58E628, Add, 0x0000004D);
		SetMemory(0x58E630, Add, 0x0000004D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000061);
		SetMemory(0x58E624, Add, 0x00000061);
		SetMemory(0x58E628, Add, 0xFFFFFFC8);
		SetMemory(0x58E630, Add, 0xFFFFFFC8);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC8);
		SetMemory(0x58E624, Add, 0xFFFFFFC8);
		SetMemory(0x58E628, Add, 0xFFFFFF9F);
		SetMemory(0x58E630, Add, 0xFFFFFF9F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF9F);
		SetMemory(0x58E624, Add, 0xFFFFFF9F);
		SetMemory(0x58E628, Add, 0x00000038);
		SetMemory(0x58E630, Add, 0x00000038);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000038);
		SetMemory(0x58E624, Add, 0x00000038);
		SetMemory(0x58E628, Add, 0x00000061);
		SetMemory(0x58E630, Add, 0x00000061);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFFB0);
		SetMemory(0x58E630, Add, 0xFFFFFFB0);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB0);
		SetMemory(0x58E624, Add, 0xFFFFFFB0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004F);
		SetMemory(0x58E624, Add, 0x0000004F);
		SetMemory(0x58E628, Add, 0xFFFFFFB1);
		SetMemory(0x58E630, Add, 0xFFFFFFB1);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB1);
		SetMemory(0x58E624, Add, 0xFFFFFFB1);
		SetMemory(0x58E628, Add, 0xFFFFFFB1);
		SetMemory(0x58E630, Add, 0xFFFFFFB1);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB1);
		SetMemory(0x58E624, Add, 0xFFFFFFB1);
		SetMemory(0x58E628, Add, 0x0000004F);
		SetMemory(0x58E630, Add, 0x0000004F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004F);
		SetMemory(0x58E624, Add, 0x0000004F);
		SetMemory(0x58E628, Add, 0x0000004F);
		SetMemory(0x58E630, Add, 0x0000004F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004D);
		SetMemory(0x58E624, Add, 0x0000004D);
		SetMemory(0x58E628, Add, 0xFFFFFFEB);
		SetMemory(0x58E630, Add, 0xFFFFFFEB);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFEB);
		SetMemory(0x58E624, Add, 0xFFFFFFEB);
		SetMemory(0x58E628, Add, 0xFFFFFFB3);
		SetMemory(0x58E630, Add, 0xFFFFFFB3);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB3);
		SetMemory(0x58E624, Add, 0xFFFFFFB3);
		SetMemory(0x58E628, Add, 0x00000015);
		SetMemory(0x58E630, Add, 0x00000015);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000015);
		SetMemory(0x58E624, Add, 0x00000015);
		SetMemory(0x58E628, Add, 0x0000004D);
		SetMemory(0x58E630, Add, 0x0000004D);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000038);
		SetMemory(0x58E624, Add, 0x00000038);
		SetMemory(0x58E628, Add, 0xFFFFFF9F);
		SetMemory(0x58E630, Add, 0xFFFFFF9F);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF9F);
		SetMemory(0x58E624, Add, 0xFFFFFF9F);
		SetMemory(0x58E628, Add, 0xFFFFFFC8);
		SetMemory(0x58E630, Add, 0xFFFFFFC8);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC8);
		SetMemory(0x58E624, Add, 0xFFFFFFC8);
		SetMemory(0x58E628, Add, 0x00000061);
		SetMemory(0x58E630, Add, 0x00000061);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000061);
		SetMemory(0x58E624, Add, 0x00000061);
		SetMemory(0x58E628, Add, 0x00000038);
		SetMemory(0x58E630, Add, 0x00000038);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000045);
		SetMemory(0x58E624, Add, 0x00000045);
		SetMemory(0x58E628, Add, 0xFFFFFFD8);
		SetMemory(0x58E630, Add, 0xFFFFFFD8);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFD8);
		SetMemory(0x58E624, Add, 0xFFFFFFD8);
		SetMemory(0x58E628, Add, 0xFFFFFFBB);
		SetMemory(0x58E630, Add, 0xFFFFFFBB);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFBB);
		SetMemory(0x58E624, Add, 0xFFFFFFBB);
		SetMemory(0x58E628, Add, 0x00000028);
		SetMemory(0x58E630, Add, 0x00000028);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000028);
		SetMemory(0x58E624, Add, 0x00000028);
		SetMemory(0x58E628, Add, 0x00000045);
		SetMemory(0x58E630, Add, 0x00000045);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001D);
		SetMemory(0x58E624, Add, 0x0000001D);
		SetMemory(0x58E628, Add, 0xFFFFFF94);
		SetMemory(0x58E630, Add, 0xFFFFFF94);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF94);
		SetMemory(0x58E624, Add, 0xFFFFFF94);
		SetMemory(0x58E628, Add, 0xFFFFFFE3);
		SetMemory(0x58E630, Add, 0xFFFFFFE3);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE3);
		SetMemory(0x58E624, Add, 0xFFFFFFE3);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Add, 0x0000001D);
		SetMemory(0x58E630, Add, 0x0000001D);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0xFFFFFFC7);
		SetMemory(0x58E630, Add, 0xFFFFFFC7);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC7);
		SetMemory(0x58E624, Add, 0xFFFFFFC7);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000039);
		SetMemory(0x58E624, Add, 0x00000039);
		SetMemory(0x58E628, Add, 0x00000039);
		SetMemory(0x58E630, Add, 0x00000039);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0xFFFFFF90);
		SetMemory(0x58E630, Add, 0xFFFFFF90);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF90);
		SetMemory(0x58E624, Add, 0xFFFFFF90);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000070);
		SetMemory(0x58E630, Add, 0x00000070);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000070);
		SetMemory(0x58E624, Add, 0x00000070);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000028);
		SetMemory(0x58E624, Add, 0x00000028);
		SetMemory(0x58E628, Add, 0xFFFFFFBB);
		SetMemory(0x58E630, Add, 0xFFFFFFBB);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFBB);
		SetMemory(0x58E624, Add, 0xFFFFFFBB);
		SetMemory(0x58E628, Add, 0xFFFFFFD8);
		SetMemory(0x58E630, Add, 0xFFFFFFD8);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFD8);
		SetMemory(0x58E624, Add, 0xFFFFFFD8);
		SetMemory(0x58E628, Add, 0x00000045);
		SetMemory(0x58E630, Add, 0x00000045);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000045);
		SetMemory(0x58E624, Add, 0x00000045);
		SetMemory(0x58E628, Add, 0x00000028);
		SetMemory(0x58E630, Add, 0x00000028);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFE3);
		SetMemory(0x58E624, Add, 0xFFFFFFE3);
		SetMemory(0x58E628, Add, 0xFFFFFF94);
		SetMemory(0x58E630, Add, 0xFFFFFF94);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF94);
		SetMemory(0x58E624, Add, 0xFFFFFF94);
		SetMemory(0x58E628, Add, 0x0000001D);
		SetMemory(0x58E630, Add, 0x0000001D);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000001D);
		SetMemory(0x58E624, Add, 0x0000001D);
		SetMemory(0x58E628, Add, 0x0000006C);
		SetMemory(0x58E630, Add, 0x0000006C);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000006C);
		SetMemory(0x58E624, Add, 0x0000006C);
		SetMemory(0x58E628, Add, 0xFFFFFFE3);
		SetMemory(0x58E630, Add, 0xFFFFFFE3);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Zealot", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000015);
		SetMemory(0x58E624, Add, 0x00000015);
		SetMemory(0x58E628, Add, 0xFFFFFFB3);
		SetMemory(0x58E630, Add, 0xFFFFFFB3);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFB3);
		SetMemory(0x58E624, Add, 0xFFFFFFB3);
		SetMemory(0x58E628, Add, 0xFFFFFFEB);
		SetMemory(0x58E630, Add, 0xFFFFFFEB);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFEB);
		SetMemory(0x58E624, Add, 0xFFFFFFEB);
		SetMemory(0x58E628, Add, 0x0000004D);
		SetMemory(0x58E630, Add, 0x0000004D);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x0000004D);
		SetMemory(0x58E624, Add, 0x0000004D);
		SetMemory(0x58E628, Add, 0x00000015);
		SetMemory(0x58E630, Add, 0x00000015);
		MoveUnit(1, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFFC8);
		SetMemory(0x58E624, Add, 0xFFFFFFC8);
		SetMemory(0x58E628, Add, 0xFFFFFF9F);
		SetMemory(0x58E630, Add, 0xFFFFFF9F);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0xFFFFFF9F);
		SetMemory(0x58E624, Add, 0xFFFFFF9F);
		SetMemory(0x58E628, Add, 0x00000038);
		SetMemory(0x58E630, Add, 0x00000038);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000038);
		SetMemory(0x58E624, Add, 0x00000038);
		SetMemory(0x58E628, Add, 0x00000061);
		SetMemory(0x58E630, Add, 0x00000061);
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000061);
		SetMemory(0x58E624, Add, 0x00000061);
		SetMemory(0x58E628, Add, 0xFFFFFFC8);
		SetMemory(0x58E630, Add, 0xFFFFFFC8);
		MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Combo");
		PreserveTrigger();
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
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
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(9, "80 + 1n Vulture", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(9, "80 + 1n Vulture", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Vulture", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(40);
		RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 5, " `SkillLoop2");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 6, " `SkillLoop2");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(300);
		SetDeaths(AllPlayers, SetTo, 5101, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000064);
		SetMemory(0x58E624, Add, 0x00000064);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000064);
		SetMemory(0x58E630, Add, 0x00000064);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000064);
		SetMemory(0x58E624, Subtract, 0x00000064);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000064);
		SetMemory(0x58E630, Subtract, 0x00000064);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000050);
		SetMemory(0x58E624, Subtract, 0x00000050);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x00000050);
		SetMemory(0x58E630, Subtract, 0x00000050);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000032);
		SetMemory(0x58E624, Add, 0x00000032);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000032);
		SetMemory(0x58E630, Add, 0x00000032);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000032);
		SetMemory(0x58E624, Subtract, 0x00000032);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000032);
		SetMemory(0x58E630, Subtract, 0x00000032);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000032);
		SetMemory(0x58E630, Add, 0x00000032);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000032);
		SetMemory(0x58E624, Subtract, 0x00000032);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000032);
		SetMemory(0x58E630, Subtract, 0x00000032);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000032);
		SetMemory(0x58E624, Add, 0x00000032);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Ghost", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Ghost", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Ghost", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000096);
		SetMemory(0x58E624, Add, 0x00000096);
		SetMemory(0x58E628, Add, 0x00000064);
		SetMemory(0x58E630, Add, 0x00000064);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000064);
		SetMemory(0x58E624, Subtract, 0x00000064);
		SetMemory(0x58E628, Add, 0x00000096);
		SetMemory(0x58E630, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000096);
		SetMemory(0x58E624, Subtract, 0x00000096);
		SetMemory(0x58E628, Subtract, 0x00000064);
		SetMemory(0x58E630, Subtract, 0x00000064);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000064);
		SetMemory(0x58E624, Add, 0x00000064);
		SetMemory(0x58E628, Subtract, 0x00000096);
		SetMemory(0x58E630, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(4, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000050);
		SetMemory(0x58E624, Add, 0x00000050);
		SetMemory(0x58E628, Add, 0x000000F0);
		SetMemory(0x58E630, Add, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000F0);
		SetMemory(0x58E624, Subtract, 0x000000F0);
		SetMemory(0x58E628, Add, 0x00000050);
		SetMemory(0x58E630, Add, 0x00000050);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000050);
		SetMemory(0x58E624, Subtract, 0x00000050);
		SetMemory(0x58E628, Subtract, 0x000000F0);
		SetMemory(0x58E630, Subtract, 0x000000F0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000F0);
		SetMemory(0x58E624, Add, 0x000000F0);
		SetMemory(0x58E628, Subtract, 0x00000050);
		SetMemory(0x58E630, Subtract, 0x00000050);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(130);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
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

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki_Bozo", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Dark Templar", CurrentPlayer, "Anywhere", Move, "05.Miyuki_Bozo");
		ModifyUnitShields(All, " * Dark Templar", CurrentPlayer, "Anywhere", 1);
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		Wait(1250);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000160);
		SetMemory(0x58E624, Add, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000160);
		SetMemory(0x58E624, Subtract, 0x00000160);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000160);
		SetMemory(0x58E630, Subtract, 0x00000160);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000160);
		SetMemory(0x58E630, Add, 0x00000160);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000140);
		SetMemory(0x58E624, Add, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000A0);
		SetMemory(0x58E624, Add, 0x000000A0);
		SetMemory(0x58E628, Subtract, 0x000000C0);
		SetMemory(0x58E630, Subtract, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000A0);
		SetMemory(0x58E624, Subtract, 0x000000A0);
		SetMemory(0x58E628, Add, 0x000000C0);
		SetMemory(0x58E630, Add, 0x000000C0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000C0);
		SetMemory(0x58E624, Subtract, 0x000000C0);
		SetMemory(0x58E628, Subtract, 0x000000A0);
		SetMemory(0x58E630, Subtract, 0x000000A0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000C0);
		SetMemory(0x58E624, Add, 0x000000C0);
		SetMemory(0x58E628, Add, 0x000000A0);
		SetMemory(0x58E630, Add, 0x000000A0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000080);
		SetMemory(0x58E624, Add, 0x00000080);
		SetMemory(0x58E628, Subtract, 0x000000E0);
		SetMemory(0x58E630, Subtract, 0x000000E0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000080);
		SetMemory(0x58E624, Subtract, 0x00000080);
		SetMemory(0x58E628, Add, 0x000000E0);
		SetMemory(0x58E630, Add, 0x000000E0);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000E0);
		SetMemory(0x58E624, Subtract, 0x000000E0);
		SetMemory(0x58E628, Subtract, 0x00000080);
		SetMemory(0x58E630, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000E0);
		SetMemory(0x58E624, Add, 0x000000E0);
		SetMemory(0x58E628, Add, 0x00000080);
		SetMemory(0x58E630, Add, 0x00000080);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000060);
		SetMemory(0x58E624, Add, 0x00000060);
		SetMemory(0x58E628, Subtract, 0x00000100);
		SetMemory(0x58E630, Subtract, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000060);
		SetMemory(0x58E624, Subtract, 0x00000060);
		SetMemory(0x58E628, Add, 0x00000100);
		SetMemory(0x58E630, Add, 0x00000100);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000100);
		SetMemory(0x58E624, Subtract, 0x00000100);
		SetMemory(0x58E628, Subtract, 0x00000060);
		SetMemory(0x58E630, Subtract, 0x00000060);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000100);
		SetMemory(0x58E624, Add, 0x00000100);
		SetMemory(0x58E628, Add, 0x00000060);
		SetMemory(0x58E630, Add, 0x00000060);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(2, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000040);
		SetMemory(0x58E624, Add, 0x00000040);
		SetMemory(0x58E628, Subtract, 0x00000120);
		SetMemory(0x58E630, Subtract, 0x00000120);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000040);
		SetMemory(0x58E624, Subtract, 0x00000040);
		SetMemory(0x58E628, Add, 0x00000120);
		SetMemory(0x58E630, Add, 0x00000120);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(2, "Protoss Observer", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "Protoss Observer", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_4", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000120);
		SetMemory(0x58E624, Subtract, 0x00000120);
		SetMemory(0x58E628, Subtract, 0x00000040);
		SetMemory(0x58E630, Subtract, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Add, 0x00000020);
		SetMemory(0x58E630, Add, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000120);
		SetMemory(0x58E624, Add, 0x00000120);
		SetMemory(0x58E628, Add, 0x00000040);
		SetMemory(0x58E630, Add, 0x00000040);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(1, "Protoss Observer", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "Protoss Observer", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Subtract, 0x00000140);
		SetMemory(0x58E630, Subtract, 0x00000140);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000020);
		SetMemory(0x58E624, Subtract, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000140);
		SetMemory(0x58E624, Subtract, 0x00000140);
		SetMemory(0x58E628, Subtract, 0x00000020);
		SetMemory(0x58E630, Subtract, 0x00000020);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000020);
		SetMemory(0x58E624, Add, 0x00000020);
		SetMemory(0x58E628, Add, 0x00000140);
		SetMemory(0x58E630, Add, 0x00000140);
		MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
		Wait(1050);
		SetDeaths(AllPlayers, SetTo, 5201, " `SkillText_Uiltimate");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000044);
		SetMemory(0x58E624, Add, 0x00000044);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000044);
		SetMemory(0x58E630, Add, 0x00000044);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000044);
		SetMemory(0x58E624, Subtract, 0x00000044);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000044);
		SetMemory(0x58E630, Subtract, 0x00000044);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000019);
		SetMemory(0x58E624, Add, 0x00000019);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000019);
		SetMemory(0x58E630, Add, 0x00000019);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000019);
		SetMemory(0x58E624, Subtract, 0x00000019);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000019);
		SetMemory(0x58E630, Subtract, 0x00000019);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Add, 0x00000070);
		SetMemory(0x58E630, Add, 0x00000070);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000070);
		SetMemory(0x58E624, Subtract, 0x00000070);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x00000070);
		SetMemory(0x58E630, Subtract, 0x00000070);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000070);
		SetMemory(0x58E624, Add, 0x00000070);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000000);
		SetMemory(0x58E624, Add, 0x00000000);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000000);
		SetMemory(0x58E630, Add, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000000);
		SetMemory(0x58E624, Subtract, 0x00000000);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000000);
		SetMemory(0x58E630, Subtract, 0x00000000);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000019);
		SetMemory(0x58E630, Add, 0x00000019);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000019);
		SetMemory(0x58E624, Subtract, 0x00000019);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000019);
		SetMemory(0x58E630, Subtract, 0x00000019);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000019);
		SetMemory(0x58E624, Add, 0x00000019);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000070);
		SetMemory(0x58E624, Add, 0x00000070);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Add, 0x00000070);
		SetMemory(0x58E630, Add, 0x00000070);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000070);
		SetMemory(0x58E624, Subtract, 0x00000070);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x00000070);
		SetMemory(0x58E630, Subtract, 0x00000070);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000076);
		SetMemory(0x58E624, Add, 0x00000076);
		SetMemory(0x58E628, Add, 0x00000044);
		SetMemory(0x58E630, Add, 0x00000044);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000044);
		SetMemory(0x58E624, Subtract, 0x00000044);
		SetMemory(0x58E628, Add, 0x00000076);
		SetMemory(0x58E630, Add, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000076);
		SetMemory(0x58E624, Subtract, 0x00000076);
		SetMemory(0x58E628, Subtract, 0x00000044);
		SetMemory(0x58E630, Subtract, 0x00000044);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000044);
		SetMemory(0x58E624, Add, 0x00000044);
		SetMemory(0x58E628, Subtract, 0x00000076);
		SetMemory(0x58E630, Subtract, 0x00000076);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_3", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_4", CurrentPlayer);
		CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x00000030);
		SetMemory(0x58E624, Add, 0x00000030);
		SetMemory(0x58E628, Add, 0x000000B0);
		SetMemory(0x58E630, Add, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x000000B0);
		SetMemory(0x58E624, Subtract, 0x000000B0);
		SetMemory(0x58E628, Add, 0x00000030);
		SetMemory(0x58E630, Add, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Subtract, 0x00000030);
		SetMemory(0x58E624, Subtract, 0x00000030);
		SetMemory(0x58E628, Subtract, 0x000000B0);
		SetMemory(0x58E630, Subtract, 0x000000B0);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		SetMemory(0x58E62C, Add, 0x000000B0);
		SetMemory(0x58E624, Add, 0x000000B0);
		SetMemory(0x58E628, Subtract, 0x00000030);
		SetMemory(0x58E630, Subtract, 0x00000030);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveUnit(8, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		MoveLocation("05.Miyuki", " * Dark Templar", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Men", CurrentPlayer, "[Skill]Unit_Wait_ALL", "05.Miyuki");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "05.Miyuki");
		Wait(50);
		KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Ultimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 2000, " * Dark Templar");
		Bring(CurrentPlayer, AtLeast, 1, " * Dark Templar", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Ultimate");
		PreserveTrigger();
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
		SetSwitch("UiltimateSwitch", Clear);
	},
}