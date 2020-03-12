
Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		SetSwitch("Recall - Ryuzu", Set);
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000018);
		SetMemory(0x58E89C, Subtract, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000018);
		SetMemory(0x58E89C, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000014);
		SetMemory(0x58E898, Add, 0x00000014);
		SetMemory(0x58E894, Subtract, 0x00000030);
		SetMemory(0x58E89C, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000014);
		SetMemory(0x58E898, Subtract, 0x00000014);
		SetMemory(0x58E894, Add, 0x00000030);
		SetMemory(0x58E89C, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000014);
		SetMemory(0x58E898, Subtract, 0x00000014);
		SetMemory(0x58E894, Subtract, 0x00000048);
		SetMemory(0x58E89C, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000014);
		SetMemory(0x58E898, Add, 0x00000014);
		SetMemory(0x58E894, Add, 0x00000048);
		SetMemory(0x58E89C, Add, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000060);
		SetMemory(0x58E89C, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000060);
		SetMemory(0x58E89C, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000018);
		SetMemory(0x58E898, Add, 0x00000018);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000018);
		SetMemory(0x58E898, Subtract, 0x00000018);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000030);
		SetMemory(0x58E898, Add, 0x00000030);
		SetMemory(0x58E894, Subtract, 0x00000014);
		SetMemory(0x58E89C, Subtract, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000030);
		SetMemory(0x58E898, Subtract, 0x00000030);
		SetMemory(0x58E894, Add, 0x00000014);
		SetMemory(0x58E89C, Add, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000048);
		SetMemory(0x58E898, Add, 0x00000048);
		SetMemory(0x58E894, Add, 0x00000014);
		SetMemory(0x58E89C, Add, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000048);
		SetMemory(0x58E898, Subtract, 0x00000048);
		SetMemory(0x58E894, Subtract, 0x00000014);
		SetMemory(0x58E89C, Subtract, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000060);
		SetMemory(0x58E898, Add, 0x00000060);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000060);
		SetMemory(0x58E898, Subtract, 0x00000060);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000018);
		SetMemory(0x58E89C, Subtract, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000018);
		SetMemory(0x58E89C, Add, 0x00000018);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000014);
		SetMemory(0x58E898, Subtract, 0x00000014);
		SetMemory(0x58E894, Subtract, 0x00000030);
		SetMemory(0x58E89C, Subtract, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000014);
		SetMemory(0x58E898, Add, 0x00000014);
		SetMemory(0x58E894, Add, 0x00000030);
		SetMemory(0x58E89C, Add, 0x00000030);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000014);
		SetMemory(0x58E898, Add, 0x00000014);
		SetMemory(0x58E894, Subtract, 0x00000048);
		SetMemory(0x58E89C, Subtract, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000014);
		SetMemory(0x58E898, Subtract, 0x00000014);
		SetMemory(0x58E894, Add, 0x00000048);
		SetMemory(0x58E89C, Add, 0x00000048);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x0000003C);
		SetMemory(0x58E898, Add, 0x0000003C);
		SetMemory(0x58E894, Subtract, 0x00000060);
		SetMemory(0x58E89C, Subtract, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x0000003C);
		SetMemory(0x58E898, Subtract, 0x0000003C);
		SetMemory(0x58E894, Add, 0x00000060);
		SetMemory(0x58E89C, Add, 0x00000060);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000064);
		SetMemory(0x58E898, Add, 0x00000064);
		SetMemory(0x58E894, Subtract, 0x00000078);
		SetMemory(0x58E89C, Subtract, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000064);
		SetMemory(0x58E898, Subtract, 0x00000064);
		SetMemory(0x58E894, Add, 0x00000078);
		SetMemory(0x58E89C, Add, 0x00000078);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000018);
		SetMemory(0x58E898, Subtract, 0x00000018);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000018);
		SetMemory(0x58E898, Add, 0x00000018);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000030);
		SetMemory(0x58E898, Subtract, 0x00000030);
		SetMemory(0x58E894, Subtract, 0x00000014);
		SetMemory(0x58E89C, Subtract, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000030);
		SetMemory(0x58E898, Add, 0x00000030);
		SetMemory(0x58E894, Add, 0x00000014);
		SetMemory(0x58E89C, Add, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000048);
		SetMemory(0x58E898, Subtract, 0x00000048);
		SetMemory(0x58E894, Add, 0x00000014);
		SetMemory(0x58E89C, Add, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000048);
		SetMemory(0x58E898, Add, 0x00000048);
		SetMemory(0x58E894, Subtract, 0x00000014);
		SetMemory(0x58E89C, Subtract, 0x00000014);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000060);
		SetMemory(0x58E898, Subtract, 0x00000060);
		SetMemory(0x58E894, Add, 0x0000003C);
		SetMemory(0x58E89C, Add, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000060);
		SetMemory(0x58E898, Add, 0x00000060);
		SetMemory(0x58E894, Subtract, 0x0000003C);
		SetMemory(0x58E89C, Subtract, 0x0000003C);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(2, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000078);
		SetMemory(0x58E898, Subtract, 0x00000078);
		SetMemory(0x58E894, Add, 0x00000064);
		SetMemory(0x58E89C, Add, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000078);
		SetMemory(0x58E898, Add, 0x00000078);
		SetMemory(0x58E894, Subtract, 0x00000064);
		SetMemory(0x58E89C, Subtract, 0x00000064);
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		RemoveUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "12.Ryuzu");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		Wait(130);
		RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Devouring One");
		Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Add, 0x00000080);
		SetMemory(0x58E898, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Subtract, 0x00000080);
		SetMemory(0x58E89C, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E890, Subtract, 0x00000080);
		SetMemory(0x58E898, Subtract, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		SetMemory(0x58E894, Add, 0x00000080);
		SetMemory(0x58E89C, Add, 0x00000080);
		MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "12.Ryuzu");
		MoveLocation("12.Ryuzu", " * Devouring One", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
		SetSwitch("Recall - Ryuzu", Clear);
		Wait(500);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}
