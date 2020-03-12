Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		MoveLocation("[Unique]Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "40 + 1n Marine", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Ghost", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, " Creep. Dunkelheit", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Goliath", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Wraith", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Firebat", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Zergling", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, " Creep. Licht", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Drone", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Mutalisk", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Guardian", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Zealot", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 3n Zeratul", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Mojo", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Gantrithor", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "40 + 1n Lurker", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "50 + 1n Tank", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, " Unit. Hoffnung 25000", "[Unique]Ryuzu", Force1);
		RemoveUnitAt(All, " Unit. Hoffnung 25000", "[Unique]Ryuzu", Force2);
		RemoveUnitAt(All, "60 + 3n Siege", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n Siege", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n Hydralisk", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n Dragoon", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n High Templar", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n Archon", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 1n Danimoth", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "60 + 3n Ghost", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, " Unit. Polarlicht", "[Unique]Ryuzu", Force1);
		RemoveUnitAt(All, " Unit. Polarlicht", "[Unique]Ryuzu", Force2);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		MoveLocation("[Unique]Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		RemoveUnitAt(All, "80 + 1n Goliath", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Vulture", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Marine", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Tom Kazansky", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Tank", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Mutalisk", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Guardian", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Artanis", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "80 + 1n Ghost", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "100 + 1n Hyperion", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "100 + 1n Dragoon", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "120 + 1n Archon", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "130 + 1n Norad", "[Unique]Ryuzu", AllPlayers);
		RemoveUnitAt(All, "130 + 1n Arbiter", "[Unique]Ryuzu", AllPlayers);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		PreserveTrigger();
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("Recall - Ryuzu", Set);
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
		SetInvincibility(Enable, " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(AllPlayers, SetTo, 12001, " `SkillText_Uiltimate");
		Wait(2000);
		SetDeaths(AllPlayers, SetTo, 12002, " `SkillText_Uiltimate");
		Wait(2500);
		SetDeaths(AllPlayers, SetTo, 12003, " `SkillText_Uiltimate");
		Wait(2500);
		SetDeaths(AllPlayers, SetTo, 12004, " `SkillText_Uiltimate");
		Wait(1500);
		SetDeaths(AllPlayers, SetTo, 12005, " `SkillText_Uiltimate");
		Wait(1500);
		SetDeaths(AllPlayers, SetTo, 12006, " `SkillText_Uiltimate");
		Wait(2000);
		SetDeaths(AllPlayers, SetTo, 12007, " `SkillText_Uiltimate");
		Wait(2500);
		SetDeaths(AllPlayers, SetTo, 12008, " `SkillText_Uiltimate");
		Wait(4500);
		SetDeaths(AllPlayers, SetTo, 12009, " `SkillText_Uiltimate");
		Wait(1200);
		SetDeaths(AllPlayers, SetTo, 12010, " `SkillText_Uiltimate");
		Wait(2800);
		SetDeaths(AllPlayers, SetTo, 12011, " `SkillText_Uiltimate");
		Wait(1200);
		SetDeaths(AllPlayers, SetTo, 12012, " `SkillText_Uiltimate");
		Wait(2200);
		SetDeaths(AllPlayers, SetTo, 12013, " `SkillText_Uiltimate");
		Wait(1000);
		SetDeaths(AllPlayers, SetTo, 12014, " `SkillText_Uiltimate");
		Wait(1700);
		SetInvincibility(Disable, " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(AllPlayers, SetTo, 12015, " `SkillText_Uiltimate");
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillCount");
		RemoveUnitAt(All, " `SystemDebuff_Slow", "Anywhere", CurrentPlayer);
		SetSwitch("Recall - Ryuzu", Clear);
		Wait(2000);
		SetDeaths(CurrentPlayer, SetTo, 3, " `SkillCount");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Bring(CurrentPlayer, AtMost, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 249, " `UltimateCoolTime");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Switch("UiltimateSwitch", Set);
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 250, " `UltimateCoolTime");
		Switch("UiltimateSwitch", Cleared);
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("UiltimateSwitch", Set);
		SetDeaths(CurrentPlayer, Subtract, 250, " `UltimateCoolTime");
		SetDeaths(CurrentPlayer, SetTo, 2160, " `UltimateCoolTime2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 330, " `SkillStep");
		SetDeaths(AllPlayers, SetTo, 12020, " `SkillText_Uiltimate");
		KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Bring(CurrentPlayer, AtMost, 1, "Protoss Arbiter", "[Skill]UseSkill");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		Wait(1000);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		RemoveUnitAt(All, " `SystemDebuff_Slow", "Anywhere", CurrentPlayer);
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, " `SystemDebuff_Slow", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000090);
		SetMemory(0x58E898, Add, 0x00000090);
		MoveUnit(1, " `SystemDebuff_Slow", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000090);
		SetMemory(0x58E89C, Subtract, 0x00000090);
		MoveUnit(1, " `SystemDebuff_Slow", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000090);
		SetMemory(0x58E898, Subtract, 0x00000090);
		MoveUnit(1, " `SystemDebuff_Slow", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000090);
		SetMemory(0x58E89C, Add, 0x00000090);
		MoveUnit(1, " `SystemDebuff_Slow", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order(" `SystemDebuff_Slow", CurrentPlayer, "Anywhere", Attack, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C0);
		SetMemory(0x58E898, Add, 0x000000C0);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x000000C0);
		SetMemory(0x58E89C, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C0);
		SetMemory(0x58E898, Subtract, 0x000000C0);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Add, 0x000000C0);
		SetMemory(0x58E89C, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000040);
		SetMemory(0x58E898, Add, 0x00000040);
		SetMemory(0x58E894, Subtract, 0x000000C0);
		SetMemory(0x58E89C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C0);
		SetMemory(0x58E898, Subtract, 0x000000C0);
		SetMemory(0x58E894, Subtract, 0x00000040);
		SetMemory(0x58E89C, Subtract, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000040);
		SetMemory(0x58E898, Subtract, 0x00000040);
		SetMemory(0x58E894, Add, 0x000000C0);
		SetMemory(0x58E89C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C0);
		SetMemory(0x58E898, Add, 0x000000C0);
		SetMemory(0x58E894, Add, 0x00000040);
		SetMemory(0x58E89C, Add, 0x00000040);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C0);
		SetMemory(0x58E898, Add, 0x000000C0);
		SetMemory(0x58E894, Subtract, 0x000000C0);
		SetMemory(0x58E89C, Subtract, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C0);
		SetMemory(0x58E898, Subtract, 0x000000C0);
		SetMemory(0x58E894, Subtract, 0x000000C0);
		SetMemory(0x58E89C, Subtract, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C0);
		SetMemory(0x58E898, Subtract, 0x000000C0);
		SetMemory(0x58E894, Add, 0x000000C0);
		SetMemory(0x58E89C, Add, 0x000000C0);
		MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C0);
		SetMemory(0x58E898, Add, 0x000000C0);
		SetMemory(0x58E894, Add, 0x000000C0);
		SetMemory(0x58E89C, Add, 0x000000C0);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
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

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("12.Ryuzu_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");
		MoveUnit(All, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu_Bozo");
		RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
		Order(" * Devouring One", CurrentPlayer, "Anywhere", Move, "12.Ryuzu_Bozo");
		ModifyUnitShields(All, " * Devouring One", CurrentPlayer, "Anywhere", 10);
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Target", "[Skill]Unit_Wait_2", CurrentPlayer);
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("Recall - Ryuzu", Set);
		Wait(1200);
		SetDeaths(AllPlayers, SetTo, 12021, " `SkillText_Uiltimate");
		Wait(1000);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000038);
		SetMemory(0x58E898, Add, 0x00000038);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000028);
		SetMemory(0x58E898, Add, 0x00000028);
		SetMemory(0x58E894, Subtract, 0x00000028);
		SetMemory(0x58E89C, Subtract, 0x00000028);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000038);
		SetMemory(0x58E89C, Subtract, 0x00000038);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000028);
		SetMemory(0x58E898, Add, 0x00000028);
		SetMemory(0x58E894, Add, 0x00000028);
		SetMemory(0x58E89C, Add, 0x00000028);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Add, 0x00000068);
		SetMemory(0x58E89C, Add, 0x00000068);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000050);
		SetMemory(0x58E898, Add, 0x00000050);
		SetMemory(0x58E894, Add, 0x00000050);
		SetMemory(0x58E89C, Add, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000068);
		SetMemory(0x58E898, Add, 0x00000068);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000071);
		SetMemory(0x58E898, Add, 0x00000071);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000068);
		SetMemory(0x58E898, Add, 0x00000068);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000050);
		SetMemory(0x58E898, Add, 0x00000050);
		SetMemory(0x58E894, Subtract, 0x00000050);
		SetMemory(0x58E89C, Subtract, 0x00000050);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x00000068);
		SetMemory(0x58E89C, Subtract, 0x00000068);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000071);
		SetMemory(0x58E89C, Subtract, 0x00000071);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Add, 0x000000A4);
		SetMemory(0x58E89C, Add, 0x000000A4);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000055);
		SetMemory(0x58E898, Add, 0x00000055);
		SetMemory(0x58E894, Add, 0x00000092);
		SetMemory(0x58E89C, Add, 0x00000092);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000092);
		SetMemory(0x58E898, Add, 0x00000092);
		SetMemory(0x58E894, Add, 0x00000055);
		SetMemory(0x58E89C, Add, 0x00000055);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A4);
		SetMemory(0x58E898, Add, 0x000000A4);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000AA);
		SetMemory(0x58E898, Add, 0x000000AA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A4);
		SetMemory(0x58E898, Add, 0x000000A4);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000092);
		SetMemory(0x58E898, Add, 0x00000092);
		SetMemory(0x58E894, Subtract, 0x00000055);
		SetMemory(0x58E89C, Subtract, 0x00000055);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000055);
		SetMemory(0x58E898, Add, 0x00000055);
		SetMemory(0x58E894, Subtract, 0x00000092);
		SetMemory(0x58E89C, Subtract, 0x00000092);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x000000A4);
		SetMemory(0x58E89C, Subtract, 0x000000A4);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x000000AA);
		SetMemory(0x58E89C, Subtract, 0x000000AA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Add, 0x000000DE);
		SetMemory(0x58E89C, Add, 0x000000DE);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000056);
		SetMemory(0x58E898, Add, 0x00000056);
		SetMemory(0x58E894, Add, 0x000000D1);
		SetMemory(0x58E89C, Add, 0x000000D1);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000007D);
		SetMemory(0x58E898, Add, 0x0000007D);
		SetMemory(0x58E894, Add, 0x000000BD);
		SetMemory(0x58E89C, Add, 0x000000BD);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A0);
		SetMemory(0x58E898, Add, 0x000000A0);
		SetMemory(0x58E894, Add, 0x000000A0);
		SetMemory(0x58E89C, Add, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000BD);
		SetMemory(0x58E898, Add, 0x000000BD);
		SetMemory(0x58E894, Add, 0x0000007D);
		SetMemory(0x58E89C, Add, 0x0000007D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D1);
		SetMemory(0x58E898, Add, 0x000000D1);
		SetMemory(0x58E894, Add, 0x00000056);
		SetMemory(0x58E89C, Add, 0x00000056);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000DE);
		SetMemory(0x58E898, Add, 0x000000DE);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E2);
		SetMemory(0x58E898, Add, 0x000000E2);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000DE);
		SetMemory(0x58E898, Add, 0x000000DE);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D1);
		SetMemory(0x58E898, Add, 0x000000D1);
		SetMemory(0x58E894, Subtract, 0x00000056);
		SetMemory(0x58E89C, Subtract, 0x00000056);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000BD);
		SetMemory(0x58E898, Add, 0x000000BD);
		SetMemory(0x58E894, Subtract, 0x0000007D);
		SetMemory(0x58E89C, Subtract, 0x0000007D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A0);
		SetMemory(0x58E898, Add, 0x000000A0);
		SetMemory(0x58E894, Subtract, 0x000000A0);
		SetMemory(0x58E89C, Subtract, 0x000000A0);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000007D);
		SetMemory(0x58E898, Add, 0x0000007D);
		SetMemory(0x58E894, Subtract, 0x000000BD);
		SetMemory(0x58E89C, Subtract, 0x000000BD);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000056);
		SetMemory(0x58E898, Add, 0x00000056);
		SetMemory(0x58E894, Subtract, 0x000000D1);
		SetMemory(0x58E89C, Subtract, 0x000000D1);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x000000DE);
		SetMemory(0x58E89C, Subtract, 0x000000DE);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x000000E2);
		SetMemory(0x58E89C, Subtract, 0x000000E2);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Add, 0x00000118);
		SetMemory(0x58E89C, Add, 0x00000118);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000058);
		SetMemory(0x58E898, Add, 0x00000058);
		SetMemory(0x58E894, Add, 0x0000010D);
		SetMemory(0x58E89C, Add, 0x0000010D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x000000FD);
		SetMemory(0x58E89C, Add, 0x000000FD);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Add, 0x000000E5);
		SetMemory(0x58E89C, Add, 0x000000E5);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E5);
		SetMemory(0x58E898, Add, 0x000000E5);
		SetMemory(0x58E894, Add, 0x000000A6);
		SetMemory(0x58E89C, Add, 0x000000A6);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FD);
		SetMemory(0x58E898, Add, 0x000000FD);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000010D);
		SetMemory(0x58E898, Add, 0x0000010D);
		SetMemory(0x58E894, Add, 0x00000058);
		SetMemory(0x58E89C, Add, 0x00000058);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000118);
		SetMemory(0x58E898, Add, 0x00000118);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000011C);
		SetMemory(0x58E898, Add, 0x0000011C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000118);
		SetMemory(0x58E898, Add, 0x00000118);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000010D);
		SetMemory(0x58E898, Add, 0x0000010D);
		SetMemory(0x58E894, Subtract, 0x00000058);
		SetMemory(0x58E89C, Subtract, 0x00000058);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FD);
		SetMemory(0x58E898, Add, 0x000000FD);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E5);
		SetMemory(0x58E898, Add, 0x000000E5);
		SetMemory(0x58E894, Subtract, 0x000000A6);
		SetMemory(0x58E89C, Subtract, 0x000000A6);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x000000E5);
		SetMemory(0x58E89C, Subtract, 0x000000E5);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x000000FD);
		SetMemory(0x58E89C, Subtract, 0x000000FD);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000058);
		SetMemory(0x58E898, Add, 0x00000058);
		SetMemory(0x58E894, Subtract, 0x0000010D);
		SetMemory(0x58E89C, Subtract, 0x0000010D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x00000118);
		SetMemory(0x58E89C, Subtract, 0x00000118);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x0000011C);
		SetMemory(0x58E89C, Subtract, 0x0000011C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(500);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000028);
		SetMemory(0x58E898, Subtract, 0x00000028);
		SetMemory(0x58E894, Subtract, 0x00000028);
		SetMemory(0x58E89C, Subtract, 0x00000028);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000038);
		SetMemory(0x58E898, Subtract, 0x00000038);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000028);
		SetMemory(0x58E898, Subtract, 0x00000028);
		SetMemory(0x58E894, Add, 0x00000028);
		SetMemory(0x58E89C, Add, 0x00000028);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000038);
		SetMemory(0x58E89C, Add, 0x00000038);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x00000068);
		SetMemory(0x58E89C, Subtract, 0x00000068);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000050);
		SetMemory(0x58E898, Subtract, 0x00000050);
		SetMemory(0x58E894, Subtract, 0x00000050);
		SetMemory(0x58E89C, Subtract, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000068);
		SetMemory(0x58E898, Subtract, 0x00000068);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000071);
		SetMemory(0x58E898, Subtract, 0x00000071);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000068);
		SetMemory(0x58E898, Subtract, 0x00000068);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000050);
		SetMemory(0x58E898, Subtract, 0x00000050);
		SetMemory(0x58E894, Add, 0x00000050);
		SetMemory(0x58E89C, Add, 0x00000050);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Add, 0x00000068);
		SetMemory(0x58E89C, Add, 0x00000068);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000071);
		SetMemory(0x58E89C, Add, 0x00000071);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x000000A4);
		SetMemory(0x58E89C, Subtract, 0x000000A4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000055);
		SetMemory(0x58E898, Subtract, 0x00000055);
		SetMemory(0x58E894, Subtract, 0x00000092);
		SetMemory(0x58E89C, Subtract, 0x00000092);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000092);
		SetMemory(0x58E898, Subtract, 0x00000092);
		SetMemory(0x58E894, Subtract, 0x00000055);
		SetMemory(0x58E89C, Subtract, 0x00000055);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A4);
		SetMemory(0x58E898, Subtract, 0x000000A4);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000AA);
		SetMemory(0x58E898, Subtract, 0x000000AA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A4);
		SetMemory(0x58E898, Subtract, 0x000000A4);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000092);
		SetMemory(0x58E898, Subtract, 0x00000092);
		SetMemory(0x58E894, Add, 0x00000055);
		SetMemory(0x58E89C, Add, 0x00000055);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000055);
		SetMemory(0x58E898, Subtract, 0x00000055);
		SetMemory(0x58E894, Add, 0x00000092);
		SetMemory(0x58E89C, Add, 0x00000092);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Add, 0x000000A4);
		SetMemory(0x58E89C, Add, 0x000000A4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x000000AA);
		SetMemory(0x58E89C, Add, 0x000000AA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x000000DE);
		SetMemory(0x58E89C, Subtract, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000056);
		SetMemory(0x58E898, Subtract, 0x00000056);
		SetMemory(0x58E894, Subtract, 0x000000D1);
		SetMemory(0x58E89C, Subtract, 0x000000D1);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000007D);
		SetMemory(0x58E898, Subtract, 0x0000007D);
		SetMemory(0x58E894, Subtract, 0x000000BD);
		SetMemory(0x58E89C, Subtract, 0x000000BD);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A0);
		SetMemory(0x58E898, Subtract, 0x000000A0);
		SetMemory(0x58E894, Subtract, 0x000000A0);
		SetMemory(0x58E89C, Subtract, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000BD);
		SetMemory(0x58E898, Subtract, 0x000000BD);
		SetMemory(0x58E894, Subtract, 0x0000007D);
		SetMemory(0x58E89C, Subtract, 0x0000007D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D1);
		SetMemory(0x58E898, Subtract, 0x000000D1);
		SetMemory(0x58E894, Subtract, 0x00000056);
		SetMemory(0x58E89C, Subtract, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000DE);
		SetMemory(0x58E898, Subtract, 0x000000DE);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E2);
		SetMemory(0x58E898, Subtract, 0x000000E2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000DE);
		SetMemory(0x58E898, Subtract, 0x000000DE);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D1);
		SetMemory(0x58E898, Subtract, 0x000000D1);
		SetMemory(0x58E894, Add, 0x00000056);
		SetMemory(0x58E89C, Add, 0x00000056);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000BD);
		SetMemory(0x58E898, Subtract, 0x000000BD);
		SetMemory(0x58E894, Add, 0x0000007D);
		SetMemory(0x58E89C, Add, 0x0000007D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A0);
		SetMemory(0x58E898, Subtract, 0x000000A0);
		SetMemory(0x58E894, Add, 0x000000A0);
		SetMemory(0x58E89C, Add, 0x000000A0);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000007D);
		SetMemory(0x58E898, Subtract, 0x0000007D);
		SetMemory(0x58E894, Add, 0x000000BD);
		SetMemory(0x58E89C, Add, 0x000000BD);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000056);
		SetMemory(0x58E898, Subtract, 0x00000056);
		SetMemory(0x58E894, Add, 0x000000D1);
		SetMemory(0x58E89C, Add, 0x000000D1);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Add, 0x000000DE);
		SetMemory(0x58E89C, Add, 0x000000DE);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x000000E2);
		SetMemory(0x58E89C, Add, 0x000000E2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x00000118);
		SetMemory(0x58E89C, Subtract, 0x00000118);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000058);
		SetMemory(0x58E898, Subtract, 0x00000058);
		SetMemory(0x58E894, Subtract, 0x0000010D);
		SetMemory(0x58E89C, Subtract, 0x0000010D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x000000FD);
		SetMemory(0x58E89C, Subtract, 0x000000FD);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x000000E5);
		SetMemory(0x58E89C, Subtract, 0x000000E5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E5);
		SetMemory(0x58E898, Subtract, 0x000000E5);
		SetMemory(0x58E894, Subtract, 0x000000A6);
		SetMemory(0x58E89C, Subtract, 0x000000A6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FD);
		SetMemory(0x58E898, Subtract, 0x000000FD);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000010D);
		SetMemory(0x58E898, Subtract, 0x0000010D);
		SetMemory(0x58E894, Subtract, 0x00000058);
		SetMemory(0x58E89C, Subtract, 0x00000058);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000118);
		SetMemory(0x58E898, Subtract, 0x00000118);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000011C);
		SetMemory(0x58E898, Subtract, 0x0000011C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000118);
		SetMemory(0x58E898, Subtract, 0x00000118);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000010D);
		SetMemory(0x58E898, Subtract, 0x0000010D);
		SetMemory(0x58E894, Add, 0x00000058);
		SetMemory(0x58E89C, Add, 0x00000058);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FD);
		SetMemory(0x58E898, Subtract, 0x000000FD);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E5);
		SetMemory(0x58E898, Subtract, 0x000000E5);
		SetMemory(0x58E894, Add, 0x000000A6);
		SetMemory(0x58E89C, Add, 0x000000A6);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Add, 0x000000E5);
		SetMemory(0x58E89C, Add, 0x000000E5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x000000FD);
		SetMemory(0x58E89C, Add, 0x000000FD);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000058);
		SetMemory(0x58E898, Subtract, 0x00000058);
		SetMemory(0x58E894, Add, 0x0000010D);
		SetMemory(0x58E89C, Add, 0x0000010D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Add, 0x00000118);
		SetMemory(0x58E89C, Add, 0x00000118);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x0000011C);
		SetMemory(0x58E89C, Add, 0x0000011C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P9);
		Wait(4500);
		GiveUnits(All, "60 + 1n Siege", P9, "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x0000015E);
		SetMemory(0x58E89C, Add, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000000F);
		SetMemory(0x58E898, Add, 0x0000000F);
		SetMemory(0x58E894, Add, 0x0000012C);
		SetMemory(0x58E89C, Add, 0x0000012C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000001E);
		SetMemory(0x58E898, Add, 0x0000001E);
		SetMemory(0x58E894, Add, 0x000000FA);
		SetMemory(0x58E89C, Add, 0x000000FA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002D);
		SetMemory(0x58E898, Add, 0x0000002D);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000004B);
		SetMemory(0x58E898, Add, 0x0000004B);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000005A);
		SetMemory(0x58E898, Add, 0x0000005A);
		SetMemory(0x58E894, Add, 0x00000032);
		SetMemory(0x58E89C, Add, 0x00000032);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000069);
		SetMemory(0x58E898, Add, 0x00000069);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000032);
		SetMemory(0x58E89C, Subtract, 0x00000032);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000087);
		SetMemory(0x58E898, Add, 0x00000087);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A5);
		SetMemory(0x58E898, Add, 0x000000A5);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000B4);
		SetMemory(0x58E898, Add, 0x000000B4);
		SetMemory(0x58E894, Subtract, 0x000000FA);
		SetMemory(0x58E89C, Subtract, 0x000000FA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C3);
		SetMemory(0x58E898, Add, 0x000000C3);
		SetMemory(0x58E894, Subtract, 0x0000012C);
		SetMemory(0x58E89C, Subtract, 0x0000012C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D2);
		SetMemory(0x58E898, Add, 0x000000D2);
		SetMemory(0x58E894, Subtract, 0x0000015E);
		SetMemory(0x58E89C, Subtract, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x0000015E);
		SetMemory(0x58E89C, Add, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000000F);
		SetMemory(0x58E898, Add, 0x0000000F);
		SetMemory(0x58E894, Add, 0x0000012C);
		SetMemory(0x58E89C, Add, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000001E);
		SetMemory(0x58E898, Add, 0x0000001E);
		SetMemory(0x58E894, Add, 0x000000FA);
		SetMemory(0x58E89C, Add, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002D);
		SetMemory(0x58E898, Add, 0x0000002D);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000004B);
		SetMemory(0x58E898, Add, 0x0000004B);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000005A);
		SetMemory(0x58E898, Add, 0x0000005A);
		SetMemory(0x58E894, Add, 0x00000032);
		SetMemory(0x58E89C, Add, 0x00000032);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000069);
		SetMemory(0x58E898, Add, 0x00000069);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000032);
		SetMemory(0x58E89C, Subtract, 0x00000032);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000087);
		SetMemory(0x58E898, Add, 0x00000087);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A5);
		SetMemory(0x58E898, Add, 0x000000A5);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 7, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000B4);
		SetMemory(0x58E898, Add, 0x000000B4);
		SetMemory(0x58E894, Subtract, 0x000000FA);
		SetMemory(0x58E89C, Subtract, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C3);
		SetMemory(0x58E898, Add, 0x000000C3);
		SetMemory(0x58E894, Subtract, 0x0000012C);
		SetMemory(0x58E89C, Subtract, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D2);
		SetMemory(0x58E898, Add, 0x000000D2);
		SetMemory(0x58E894, Subtract, 0x0000015E);
		SetMemory(0x58E89C, Subtract, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 8, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000B4);
		SetMemory(0x58E898, Add, 0x000000B4);
		SetMemory(0x58E894, Subtract, 0x000000FA);
		SetMemory(0x58E89C, Subtract, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C3);
		SetMemory(0x58E898, Add, 0x000000C3);
		SetMemory(0x58E894, Subtract, 0x0000012C);
		SetMemory(0x58E89C, Subtract, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D2);
		SetMemory(0x58E898, Add, 0x000000D2);
		SetMemory(0x58E894, Subtract, 0x0000015E);
		SetMemory(0x58E89C, Subtract, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Subtract, 0x0000000F);
		SetMemory(0x58E89C, Subtract, 0x0000000F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Subtract, 0x0000001E);
		SetMemory(0x58E89C, Subtract, 0x0000001E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x0000002D);
		SetMemory(0x58E89C, Subtract, 0x0000002D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x0000004B);
		SetMemory(0x58E89C, Subtract, 0x0000004B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000032);
		SetMemory(0x58E898, Add, 0x00000032);
		SetMemory(0x58E894, Subtract, 0x0000005A);
		SetMemory(0x58E89C, Subtract, 0x0000005A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000069);
		SetMemory(0x58E89C, Subtract, 0x00000069);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000032);
		SetMemory(0x58E898, Subtract, 0x00000032);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x00000087);
		SetMemory(0x58E89C, Subtract, 0x00000087);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000A5);
		SetMemory(0x58E89C, Subtract, 0x000000A5);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FA);
		SetMemory(0x58E898, Subtract, 0x000000FA);
		SetMemory(0x58E894, Subtract, 0x000000B4);
		SetMemory(0x58E89C, Subtract, 0x000000B4);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000012C);
		SetMemory(0x58E898, Subtract, 0x0000012C);
		SetMemory(0x58E894, Subtract, 0x000000C3);
		SetMemory(0x58E89C, Subtract, 0x000000C3);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000015E);
		SetMemory(0x58E898, Subtract, 0x0000015E);
		SetMemory(0x58E894, Subtract, 0x000000D2);
		SetMemory(0x58E89C, Subtract, 0x000000D2);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Subtract, 0x0000000F);
		SetMemory(0x58E89C, Subtract, 0x0000000F);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Subtract, 0x0000001E);
		SetMemory(0x58E89C, Subtract, 0x0000001E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x0000002D);
		SetMemory(0x58E89C, Subtract, 0x0000002D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x0000004B);
		SetMemory(0x58E89C, Subtract, 0x0000004B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000032);
		SetMemory(0x58E898, Add, 0x00000032);
		SetMemory(0x58E894, Subtract, 0x0000005A);
		SetMemory(0x58E89C, Subtract, 0x0000005A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000069);
		SetMemory(0x58E89C, Subtract, 0x00000069);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000032);
		SetMemory(0x58E898, Subtract, 0x00000032);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x00000087);
		SetMemory(0x58E89C, Subtract, 0x00000087);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000A5);
		SetMemory(0x58E89C, Subtract, 0x000000A5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 7, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FA);
		SetMemory(0x58E898, Subtract, 0x000000FA);
		SetMemory(0x58E894, Subtract, 0x000000B4);
		SetMemory(0x58E89C, Subtract, 0x000000B4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000012C);
		SetMemory(0x58E898, Subtract, 0x0000012C);
		SetMemory(0x58E894, Subtract, 0x000000C3);
		SetMemory(0x58E89C, Subtract, 0x000000C3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000015E);
		SetMemory(0x58E898, Subtract, 0x0000015E);
		SetMemory(0x58E894, Subtract, 0x000000D2);
		SetMemory(0x58E89C, Subtract, 0x000000D2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 8, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FA);
		SetMemory(0x58E898, Subtract, 0x000000FA);
		SetMemory(0x58E894, Subtract, 0x000000B4);
		SetMemory(0x58E89C, Subtract, 0x000000B4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000012C);
		SetMemory(0x58E898, Subtract, 0x0000012C);
		SetMemory(0x58E894, Subtract, 0x000000C3);
		SetMemory(0x58E89C, Subtract, 0x000000C3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000015E);
		SetMemory(0x58E898, Subtract, 0x0000015E);
		SetMemory(0x58E894, Subtract, 0x000000D2);
		SetMemory(0x58E89C, Subtract, 0x000000D2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x0000015E);
		SetMemory(0x58E89C, Subtract, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000000F);
		SetMemory(0x58E898, Subtract, 0x0000000F);
		SetMemory(0x58E894, Subtract, 0x0000012C);
		SetMemory(0x58E89C, Subtract, 0x0000012C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000001E);
		SetMemory(0x58E898, Subtract, 0x0000001E);
		SetMemory(0x58E894, Subtract, 0x000000FA);
		SetMemory(0x58E89C, Subtract, 0x000000FA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002D);
		SetMemory(0x58E898, Subtract, 0x0000002D);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000004B);
		SetMemory(0x58E898, Subtract, 0x0000004B);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000005A);
		SetMemory(0x58E898, Subtract, 0x0000005A);
		SetMemory(0x58E894, Subtract, 0x00000032);
		SetMemory(0x58E89C, Subtract, 0x00000032);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000069);
		SetMemory(0x58E898, Subtract, 0x00000069);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000032);
		SetMemory(0x58E89C, Add, 0x00000032);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000087);
		SetMemory(0x58E898, Subtract, 0x00000087);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A5);
		SetMemory(0x58E898, Subtract, 0x000000A5);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000B4);
		SetMemory(0x58E898, Subtract, 0x000000B4);
		SetMemory(0x58E894, Add, 0x000000FA);
		SetMemory(0x58E89C, Add, 0x000000FA);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C3);
		SetMemory(0x58E898, Subtract, 0x000000C3);
		SetMemory(0x58E894, Add, 0x0000012C);
		SetMemory(0x58E89C, Add, 0x0000012C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D2);
		SetMemory(0x58E898, Subtract, 0x000000D2);
		SetMemory(0x58E894, Add, 0x0000015E);
		SetMemory(0x58E89C, Add, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x0000015E);
		SetMemory(0x58E89C, Subtract, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000000F);
		SetMemory(0x58E898, Subtract, 0x0000000F);
		SetMemory(0x58E894, Subtract, 0x0000012C);
		SetMemory(0x58E89C, Subtract, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000001E);
		SetMemory(0x58E898, Subtract, 0x0000001E);
		SetMemory(0x58E894, Subtract, 0x000000FA);
		SetMemory(0x58E89C, Subtract, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002D);
		SetMemory(0x58E898, Subtract, 0x0000002D);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000096);
		SetMemory(0x58E89C, Subtract, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000004B);
		SetMemory(0x58E898, Subtract, 0x0000004B);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000005A);
		SetMemory(0x58E898, Subtract, 0x0000005A);
		SetMemory(0x58E894, Subtract, 0x00000032);
		SetMemory(0x58E89C, Subtract, 0x00000032);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000069);
		SetMemory(0x58E898, Subtract, 0x00000069);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000032);
		SetMemory(0x58E89C, Add, 0x00000032);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000087);
		SetMemory(0x58E898, Subtract, 0x00000087);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A5);
		SetMemory(0x58E898, Subtract, 0x000000A5);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 7, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000B4);
		SetMemory(0x58E898, Subtract, 0x000000B4);
		SetMemory(0x58E894, Add, 0x000000FA);
		SetMemory(0x58E89C, Add, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C3);
		SetMemory(0x58E898, Subtract, 0x000000C3);
		SetMemory(0x58E894, Add, 0x0000012C);
		SetMemory(0x58E89C, Add, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D2);
		SetMemory(0x58E898, Subtract, 0x000000D2);
		SetMemory(0x58E894, Add, 0x0000015E);
		SetMemory(0x58E89C, Add, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 8, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000B4);
		SetMemory(0x58E898, Subtract, 0x000000B4);
		SetMemory(0x58E894, Add, 0x000000FA);
		SetMemory(0x58E89C, Add, 0x000000FA);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C3);
		SetMemory(0x58E898, Subtract, 0x000000C3);
		SetMemory(0x58E894, Add, 0x0000012C);
		SetMemory(0x58E89C, Add, 0x0000012C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D2);
		SetMemory(0x58E898, Subtract, 0x000000D2);
		SetMemory(0x58E894, Add, 0x0000015E);
		SetMemory(0x58E89C, Add, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 3, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000015E);
		SetMemory(0x58E898, Subtract, 0x0000015E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000012C);
		SetMemory(0x58E898, Subtract, 0x0000012C);
		SetMemory(0x58E894, Add, 0x0000000F);
		SetMemory(0x58E89C, Add, 0x0000000F);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FA);
		SetMemory(0x58E898, Subtract, 0x000000FA);
		SetMemory(0x58E894, Add, 0x0000001E);
		SetMemory(0x58E89C, Add, 0x0000001E);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Add, 0x0000002D);
		SetMemory(0x58E89C, Add, 0x0000002D);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Add, 0x0000004B);
		SetMemory(0x58E89C, Add, 0x0000004B);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000032);
		SetMemory(0x58E898, Subtract, 0x00000032);
		SetMemory(0x58E894, Add, 0x0000005A);
		SetMemory(0x58E89C, Add, 0x0000005A);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000069);
		SetMemory(0x58E89C, Add, 0x00000069);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000032);
		SetMemory(0x58E898, Add, 0x00000032);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Add, 0x00000087);
		SetMemory(0x58E89C, Add, 0x00000087);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000A5);
		SetMemory(0x58E89C, Add, 0x000000A5);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Add, 0x000000B4);
		SetMemory(0x58E89C, Add, 0x000000B4);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Add, 0x000000C3);
		SetMemory(0x58E89C, Add, 0x000000C3);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		SetMemory(0x58E894, Add, 0x000000D2);
		SetMemory(0x58E89C, Add, 0x000000D2);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000015E);
		SetMemory(0x58E898, Subtract, 0x0000015E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000012C);
		SetMemory(0x58E898, Subtract, 0x0000012C);
		SetMemory(0x58E894, Add, 0x0000000F);
		SetMemory(0x58E89C, Add, 0x0000000F);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FA);
		SetMemory(0x58E898, Subtract, 0x000000FA);
		SetMemory(0x58E894, Add, 0x0000001E);
		SetMemory(0x58E89C, Add, 0x0000001E);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Add, 0x0000002D);
		SetMemory(0x58E89C, Add, 0x0000002D);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000096);
		SetMemory(0x58E898, Subtract, 0x00000096);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Add, 0x0000004B);
		SetMemory(0x58E89C, Add, 0x0000004B);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000032);
		SetMemory(0x58E898, Subtract, 0x00000032);
		SetMemory(0x58E894, Add, 0x0000005A);
		SetMemory(0x58E89C, Add, 0x0000005A);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000069);
		SetMemory(0x58E89C, Add, 0x00000069);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000032);
		SetMemory(0x58E898, Add, 0x00000032);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Add, 0x00000087);
		SetMemory(0x58E89C, Add, 0x00000087);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000096);
		SetMemory(0x58E898, Add, 0x00000096);
		SetMemory(0x58E894, Add, 0x00000096);
		SetMemory(0x58E89C, Add, 0x00000096);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000A5);
		SetMemory(0x58E89C, Add, 0x000000A5);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtMost, 8, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Add, 0x000000B4);
		SetMemory(0x58E89C, Add, 0x000000B4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Add, 0x000000C3);
		SetMemory(0x58E89C, Add, 0x000000C3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		SetMemory(0x58E894, Add, 0x000000D2);
		SetMemory(0x58E89C, Add, 0x000000D2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 11, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 9, " `SkillLoop2");
		Deaths(CurrentPlayer, AtMost, 14, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Add, 0x000000B4);
		SetMemory(0x58E89C, Add, 0x000000B4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Add, 0x000000C3);
		SetMemory(0x58E89C, Add, 0x000000C3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		SetMemory(0x58E894, Add, 0x000000D2);
		SetMemory(0x58E89C, Add, 0x000000D2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 11, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 4, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 18, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 15, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FA);
		SetMemory(0x58E898, Add, 0x000000FA);
		SetMemory(0x58E894, Add, 0x000000B4);
		SetMemory(0x58E89C, Add, 0x000000B4);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000012C);
		SetMemory(0x58E898, Add, 0x0000012C);
		SetMemory(0x58E894, Add, 0x000000C3);
		SetMemory(0x58E89C, Add, 0x000000C3);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000015E);
		SetMemory(0x58E898, Add, 0x0000015E);
		SetMemory(0x58E894, Add, 0x000000D2);
		SetMemory(0x58E89C, Add, 0x000000D2);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(0);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
		Wait(100);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 19, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000038);
		SetMemory(0x58E898, Add, 0x00000038);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000028);
		SetMemory(0x58E898, Add, 0x00000028);
		SetMemory(0x58E894, Subtract, 0x00000028);
		SetMemory(0x58E89C, Subtract, 0x00000028);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000038);
		SetMemory(0x58E89C, Subtract, 0x00000038);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000028);
		SetMemory(0x58E898, Add, 0x00000028);
		SetMemory(0x58E894, Add, 0x00000028);
		SetMemory(0x58E89C, Add, 0x00000028);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Add, 0x00000068);
		SetMemory(0x58E89C, Add, 0x00000068);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000050);
		SetMemory(0x58E898, Add, 0x00000050);
		SetMemory(0x58E894, Add, 0x00000050);
		SetMemory(0x58E89C, Add, 0x00000050);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000068);
		SetMemory(0x58E898, Add, 0x00000068);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000071);
		SetMemory(0x58E898, Add, 0x00000071);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 20, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000068);
		SetMemory(0x58E898, Add, 0x00000068);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000050);
		SetMemory(0x58E898, Add, 0x00000050);
		SetMemory(0x58E894, Subtract, 0x00000050);
		SetMemory(0x58E89C, Subtract, 0x00000050);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x00000068);
		SetMemory(0x58E89C, Subtract, 0x00000068);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000071);
		SetMemory(0x58E89C, Subtract, 0x00000071);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Add, 0x000000A4);
		SetMemory(0x58E89C, Add, 0x000000A4);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000055);
		SetMemory(0x58E898, Add, 0x00000055);
		SetMemory(0x58E894, Add, 0x00000092);
		SetMemory(0x58E89C, Add, 0x00000092);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000092);
		SetMemory(0x58E898, Add, 0x00000092);
		SetMemory(0x58E894, Add, 0x00000055);
		SetMemory(0x58E89C, Add, 0x00000055);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A4);
		SetMemory(0x58E898, Add, 0x000000A4);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000AA);
		SetMemory(0x58E898, Add, 0x000000AA);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A4);
		SetMemory(0x58E898, Add, 0x000000A4);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000092);
		SetMemory(0x58E898, Add, 0x00000092);
		SetMemory(0x58E894, Subtract, 0x00000055);
		SetMemory(0x58E89C, Subtract, 0x00000055);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 21, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000055);
		SetMemory(0x58E898, Add, 0x00000055);
		SetMemory(0x58E894, Subtract, 0x00000092);
		SetMemory(0x58E89C, Subtract, 0x00000092);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002A);
		SetMemory(0x58E898, Add, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x000000A4);
		SetMemory(0x58E89C, Subtract, 0x000000A4);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x000000AA);
		SetMemory(0x58E89C, Subtract, 0x000000AA);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Add, 0x000000DE);
		SetMemory(0x58E89C, Add, 0x000000DE);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000056);
		SetMemory(0x58E898, Add, 0x00000056);
		SetMemory(0x58E894, Add, 0x000000D1);
		SetMemory(0x58E89C, Add, 0x000000D1);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000007D);
		SetMemory(0x58E898, Add, 0x0000007D);
		SetMemory(0x58E894, Add, 0x000000BD);
		SetMemory(0x58E89C, Add, 0x000000BD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A0);
		SetMemory(0x58E898, Add, 0x000000A0);
		SetMemory(0x58E894, Add, 0x000000A0);
		SetMemory(0x58E89C, Add, 0x000000A0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000BD);
		SetMemory(0x58E898, Add, 0x000000BD);
		SetMemory(0x58E894, Add, 0x0000007D);
		SetMemory(0x58E89C, Add, 0x0000007D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D1);
		SetMemory(0x58E898, Add, 0x000000D1);
		SetMemory(0x58E894, Add, 0x00000056);
		SetMemory(0x58E89C, Add, 0x00000056);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000DE);
		SetMemory(0x58E898, Add, 0x000000DE);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E2);
		SetMemory(0x58E898, Add, 0x000000E2);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000DE);
		SetMemory(0x58E898, Add, 0x000000DE);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000D1);
		SetMemory(0x58E898, Add, 0x000000D1);
		SetMemory(0x58E894, Subtract, 0x00000056);
		SetMemory(0x58E89C, Subtract, 0x00000056);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000BD);
		SetMemory(0x58E898, Add, 0x000000BD);
		SetMemory(0x58E894, Subtract, 0x0000007D);
		SetMemory(0x58E89C, Subtract, 0x0000007D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A0);
		SetMemory(0x58E898, Add, 0x000000A0);
		SetMemory(0x58E894, Subtract, 0x000000A0);
		SetMemory(0x58E89C, Subtract, 0x000000A0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 22, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000007D);
		SetMemory(0x58E898, Add, 0x0000007D);
		SetMemory(0x58E894, Subtract, 0x000000BD);
		SetMemory(0x58E89C, Subtract, 0x000000BD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000056);
		SetMemory(0x58E898, Add, 0x00000056);
		SetMemory(0x58E894, Subtract, 0x000000D1);
		SetMemory(0x58E89C, Subtract, 0x000000D1);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x000000DE);
		SetMemory(0x58E89C, Subtract, 0x000000DE);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x000000E2);
		SetMemory(0x58E89C, Subtract, 0x000000E2);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Add, 0x00000118);
		SetMemory(0x58E89C, Add, 0x00000118);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000058);
		SetMemory(0x58E898, Add, 0x00000058);
		SetMemory(0x58E894, Add, 0x0000010D);
		SetMemory(0x58E89C, Add, 0x0000010D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x000000FD);
		SetMemory(0x58E89C, Add, 0x000000FD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Add, 0x000000E5);
		SetMemory(0x58E89C, Add, 0x000000E5);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E5);
		SetMemory(0x58E898, Add, 0x000000E5);
		SetMemory(0x58E894, Add, 0x000000A6);
		SetMemory(0x58E89C, Add, 0x000000A6);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FD);
		SetMemory(0x58E898, Add, 0x000000FD);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000010D);
		SetMemory(0x58E898, Add, 0x0000010D);
		SetMemory(0x58E894, Add, 0x00000058);
		SetMemory(0x58E89C, Add, 0x00000058);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000118);
		SetMemory(0x58E898, Add, 0x00000118);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000011C);
		SetMemory(0x58E898, Add, 0x0000011C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000118);
		SetMemory(0x58E898, Add, 0x00000118);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000010D);
		SetMemory(0x58E898, Add, 0x0000010D);
		SetMemory(0x58E894, Subtract, 0x00000058);
		SetMemory(0x58E89C, Subtract, 0x00000058);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000FD);
		SetMemory(0x58E898, Add, 0x000000FD);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000E5);
		SetMemory(0x58E898, Add, 0x000000E5);
		SetMemory(0x58E894, Subtract, 0x000000A6);
		SetMemory(0x58E89C, Subtract, 0x000000A6);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C8);
		SetMemory(0x58E898, Add, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x000000E5);
		SetMemory(0x58E89C, Subtract, 0x000000E5);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 23, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x000000FD);
		SetMemory(0x58E89C, Subtract, 0x000000FD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000058);
		SetMemory(0x58E898, Add, 0x00000058);
		SetMemory(0x58E894, Subtract, 0x0000010D);
		SetMemory(0x58E89C, Subtract, 0x0000010D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000002C);
		SetMemory(0x58E898, Add, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x00000118);
		SetMemory(0x58E89C, Subtract, 0x00000118);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x0000011C);
		SetMemory(0x58E89C, Subtract, 0x0000011C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 24, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000028);
		SetMemory(0x58E898, Subtract, 0x00000028);
		SetMemory(0x58E894, Subtract, 0x00000028);
		SetMemory(0x58E89C, Subtract, 0x00000028);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000038);
		SetMemory(0x58E898, Subtract, 0x00000038);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000028);
		SetMemory(0x58E898, Subtract, 0x00000028);
		SetMemory(0x58E894, Add, 0x00000028);
		SetMemory(0x58E89C, Add, 0x00000028);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000038);
		SetMemory(0x58E89C, Add, 0x00000038);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x00000068);
		SetMemory(0x58E89C, Subtract, 0x00000068);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000050);
		SetMemory(0x58E898, Subtract, 0x00000050);
		SetMemory(0x58E894, Subtract, 0x00000050);
		SetMemory(0x58E89C, Subtract, 0x00000050);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000068);
		SetMemory(0x58E898, Subtract, 0x00000068);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000071);
		SetMemory(0x58E898, Subtract, 0x00000071);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 25, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000068);
		SetMemory(0x58E898, Subtract, 0x00000068);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000050);
		SetMemory(0x58E898, Subtract, 0x00000050);
		SetMemory(0x58E894, Add, 0x00000050);
		SetMemory(0x58E89C, Add, 0x00000050);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Add, 0x00000068);
		SetMemory(0x58E89C, Add, 0x00000068);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000071);
		SetMemory(0x58E89C, Add, 0x00000071);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Subtract, 0x000000A4);
		SetMemory(0x58E89C, Subtract, 0x000000A4);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000055);
		SetMemory(0x58E898, Subtract, 0x00000055);
		SetMemory(0x58E894, Subtract, 0x00000092);
		SetMemory(0x58E89C, Subtract, 0x00000092);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000092);
		SetMemory(0x58E898, Subtract, 0x00000092);
		SetMemory(0x58E894, Subtract, 0x00000055);
		SetMemory(0x58E89C, Subtract, 0x00000055);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A4);
		SetMemory(0x58E898, Subtract, 0x000000A4);
		SetMemory(0x58E894, Subtract, 0x0000002A);
		SetMemory(0x58E89C, Subtract, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000AA);
		SetMemory(0x58E898, Subtract, 0x000000AA);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A4);
		SetMemory(0x58E898, Subtract, 0x000000A4);
		SetMemory(0x58E894, Add, 0x0000002A);
		SetMemory(0x58E89C, Add, 0x0000002A);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000092);
		SetMemory(0x58E898, Subtract, 0x00000092);
		SetMemory(0x58E894, Add, 0x00000055);
		SetMemory(0x58E89C, Add, 0x00000055);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 26, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000055);
		SetMemory(0x58E898, Subtract, 0x00000055);
		SetMemory(0x58E894, Add, 0x00000092);
		SetMemory(0x58E89C, Add, 0x00000092);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002A);
		SetMemory(0x58E898, Subtract, 0x0000002A);
		SetMemory(0x58E894, Add, 0x000000A4);
		SetMemory(0x58E89C, Add, 0x000000A4);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x000000AA);
		SetMemory(0x58E89C, Add, 0x000000AA);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x000000DE);
		SetMemory(0x58E89C, Subtract, 0x000000DE);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000056);
		SetMemory(0x58E898, Subtract, 0x00000056);
		SetMemory(0x58E894, Subtract, 0x000000D1);
		SetMemory(0x58E89C, Subtract, 0x000000D1);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000007D);
		SetMemory(0x58E898, Subtract, 0x0000007D);
		SetMemory(0x58E894, Subtract, 0x000000BD);
		SetMemory(0x58E89C, Subtract, 0x000000BD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A0);
		SetMemory(0x58E898, Subtract, 0x000000A0);
		SetMemory(0x58E894, Subtract, 0x000000A0);
		SetMemory(0x58E89C, Subtract, 0x000000A0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000BD);
		SetMemory(0x58E898, Subtract, 0x000000BD);
		SetMemory(0x58E894, Subtract, 0x0000007D);
		SetMemory(0x58E89C, Subtract, 0x0000007D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D1);
		SetMemory(0x58E898, Subtract, 0x000000D1);
		SetMemory(0x58E894, Subtract, 0x00000056);
		SetMemory(0x58E89C, Subtract, 0x00000056);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000DE);
		SetMemory(0x58E898, Subtract, 0x000000DE);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E2);
		SetMemory(0x58E898, Subtract, 0x000000E2);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000DE);
		SetMemory(0x58E898, Subtract, 0x000000DE);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000D1);
		SetMemory(0x58E898, Subtract, 0x000000D1);
		SetMemory(0x58E894, Add, 0x00000056);
		SetMemory(0x58E89C, Add, 0x00000056);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000BD);
		SetMemory(0x58E898, Subtract, 0x000000BD);
		SetMemory(0x58E894, Add, 0x0000007D);
		SetMemory(0x58E89C, Add, 0x0000007D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A0);
		SetMemory(0x58E898, Subtract, 0x000000A0);
		SetMemory(0x58E894, Add, 0x000000A0);
		SetMemory(0x58E89C, Add, 0x000000A0);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 27, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000007D);
		SetMemory(0x58E898, Subtract, 0x0000007D);
		SetMemory(0x58E894, Add, 0x000000BD);
		SetMemory(0x58E89C, Add, 0x000000BD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000056);
		SetMemory(0x58E898, Subtract, 0x00000056);
		SetMemory(0x58E894, Add, 0x000000D1);
		SetMemory(0x58E89C, Add, 0x000000D1);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Add, 0x000000DE);
		SetMemory(0x58E89C, Add, 0x000000DE);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x000000E2);
		SetMemory(0x58E89C, Add, 0x000000E2);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Subtract, 0x00000118);
		SetMemory(0x58E89C, Subtract, 0x00000118);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000058);
		SetMemory(0x58E898, Subtract, 0x00000058);
		SetMemory(0x58E894, Subtract, 0x0000010D);
		SetMemory(0x58E89C, Subtract, 0x0000010D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x000000FD);
		SetMemory(0x58E89C, Subtract, 0x000000FD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x000000E5);
		SetMemory(0x58E89C, Subtract, 0x000000E5);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Subtract, 0x000000C8);
		SetMemory(0x58E89C, Subtract, 0x000000C8);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E5);
		SetMemory(0x58E898, Subtract, 0x000000E5);
		SetMemory(0x58E894, Subtract, 0x000000A6);
		SetMemory(0x58E89C, Subtract, 0x000000A6);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FD);
		SetMemory(0x58E898, Subtract, 0x000000FD);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000010D);
		SetMemory(0x58E898, Subtract, 0x0000010D);
		SetMemory(0x58E894, Subtract, 0x00000058);
		SetMemory(0x58E89C, Subtract, 0x00000058);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000118);
		SetMemory(0x58E898, Subtract, 0x00000118);
		SetMemory(0x58E894, Subtract, 0x0000002C);
		SetMemory(0x58E89C, Subtract, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000011C);
		SetMemory(0x58E898, Subtract, 0x0000011C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000118);
		SetMemory(0x58E898, Subtract, 0x00000118);
		SetMemory(0x58E894, Add, 0x0000002C);
		SetMemory(0x58E89C, Add, 0x0000002C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000010D);
		SetMemory(0x58E898, Subtract, 0x0000010D);
		SetMemory(0x58E894, Add, 0x00000058);
		SetMemory(0x58E89C, Add, 0x00000058);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000FD);
		SetMemory(0x58E898, Subtract, 0x000000FD);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000E5);
		SetMemory(0x58E898, Subtract, 0x000000E5);
		SetMemory(0x58E894, Add, 0x000000A6);
		SetMemory(0x58E89C, Add, 0x000000A6);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C8);
		SetMemory(0x58E898, Subtract, 0x000000C8);
		SetMemory(0x58E894, Add, 0x000000C8);
		SetMemory(0x58E89C, Add, 0x000000C8);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Add, 0x000000E5);
		SetMemory(0x58E89C, Add, 0x000000E5);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 28, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_5", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x000000FD);
		SetMemory(0x58E89C, Add, 0x000000FD);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000058);
		SetMemory(0x58E898, Subtract, 0x00000058);
		SetMemory(0x58E894, Add, 0x0000010D);
		SetMemory(0x58E89C, Add, 0x0000010D);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000002C);
		SetMemory(0x58E898, Subtract, 0x0000002C);
		SetMemory(0x58E894, Add, 0x00000118);
		SetMemory(0x58E89C, Add, 0x00000118);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x0000011C);
		SetMemory(0x58E89C, Add, 0x0000011C);
		MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		Wait(250);
		KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
		Wait(0);
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

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 29, " `SkillCount");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("UiltimateSwitch", Clear);
		SetSwitch("Recall - Ryuzu", Clear);
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
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "Protoss Shuttle", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Terran Dropship", "[Skill]Unit_Wait_2", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x000000C0);
		SetMemory(0x58E89C, Add, 0x000000C0);
		MoveUnit(9, "Protoss Shuttle", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x000000C0);
		SetMemory(0x58E89C, Subtract, 0x000000C0);
		MoveUnit(9, "Terran Dropship", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Terran Dropship", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Shuttle", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "Protoss Shuttle", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Terran Dropship", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Add, 0x00000060);
		SetMemory(0x58E89C, Add, 0x00000060);
		MoveUnit(9, "Protoss Shuttle", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x00000060);
		SetMemory(0x58E89C, Subtract, 0x00000060);
		MoveUnit(9, "Terran Dropship", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Terran Dropship", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Shuttle", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "Protoss Shuttle", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Terran Dropship", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000A6);
		SetMemory(0x58E898, Subtract, 0x000000A6);
		SetMemory(0x58E894, Subtract, 0x00000060);
		SetMemory(0x58E89C, Subtract, 0x00000060);
		MoveUnit(9, "Protoss Shuttle", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000A6);
		SetMemory(0x58E898, Add, 0x000000A6);
		SetMemory(0x58E894, Add, 0x00000060);
		SetMemory(0x58E89C, Add, 0x00000060);
		MoveUnit(9, "Terran Dropship", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Terran Dropship", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Shuttle", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop3");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(9, "Protoss Shuttle", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(9, "Terran Dropship", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x000000C0);
		SetMemory(0x58E898, Add, 0x000000C0);
		MoveUnit(9, "Protoss Shuttle", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x000000C0);
		SetMemory(0x58E898, Subtract, 0x000000C0);
		MoveUnit(9, "Terran Dropship", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Terran Dropship", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Protoss Shuttle", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
	},
}
