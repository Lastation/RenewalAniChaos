Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		MoveLocation("09.HotoMoka_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		KillUnit("Protoss Observer", CurrentPlayer);
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka_Bozo");
		RemoveUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
		Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "09.HotoMoka_Bozo");
		KillUnit("Protoss Observer", CurrentPlayer);
		MoveUnit(All, "100 + 1n Hyperion", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
	},
}

Trigger { -- Skill : Uiltimate
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetSwitch("Recall - Moka", Set);
		Wait(4500);
		SetSwitch("Recall - Moka", Clear);
		CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		RemoveUnitAt(All, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

x = 64;
y = 0;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, " Unit. Schnee", CurrentPlayer, "Anywhere", P12);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 1, 1 do

x = 64 * (2 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnitWithProperties(24, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
		CreateUnitWithProperties(24, "40 + 1n Lurker", "[Skill]Unit_Wait_7", CurrentPlayer, {
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
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(12, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(12, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(12, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(12, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 4, 1 do

x = 32 * (5 - i);
y = 32 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, "60 + 1n High Templar", CurrentPlayer, "Anywhere", P12);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 2, 1 do

x = 64 * (3 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 3, 1 do

x = 64 * (4 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Tank", CurrentPlayer, "Anywhere", P12);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 4, 1 do

x = 64 * (5 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 10, 1 do

x = 32 * (11 - i);
y = 32 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, "60 + 1n Hydralisk", CurrentPlayer, "Anywhere", P12);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 5, 1 do

x = 64 * (6 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 6, 1 do

x = 64 * (7 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		GiveUnits(All, "60 + 3n Siege", CurrentPlayer, "Anywhere", P12);
		KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
		Wait(2500);
		GiveUnits(All, "60 + 1n Hydralisk", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "80 + 1n Tank", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 1n High Templar", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, " Unit. Schnee", P12, "Anywhere", CurrentPlayer);
		GiveUnits(All, "60 + 3n Siege", P12, "Anywhere", CurrentPlayer);
		Wait(0);
		Order("60 + 1n Hydralisk", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Order("80 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Order(" Unit. Schnee", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 6, 1 do

x = 64 * (7 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end


Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 5, 1 do

x = 64 * (6 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end


Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 4, 1 do

x = 64 * (5 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 3, 1 do

x = 64 * (4 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}



for i = 0, 2, 1 do

x = 64 * (3 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end


Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


for i = 0, 1, 1 do

x = 64 * (2 - i);
y = 64 * i;

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

end

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 15, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}


x = 64;
y = 0

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(4, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, x, y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -y, x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, -x, -y);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		LMove(147, y, -x);
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		RemoveUnitAt(all, "Men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 16, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
		Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
	},
}



Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 10, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Wait(130);
		SetDeaths(CurrentPlayer, SetTo, 10, " `SkillCount");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
	},
}

Trigger {
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Infested Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 17, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
	},
	actions = {
		Comment("Skill : Uiltimate");
		PreserveTrigger();
		CreateUnit(1, "100 + 1n Hyperion", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
		MoveUnit(1, "100 + 1n Hyperion", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		Order("100 + 1n Hyperion", CurrentPlayer, "Anywhere", Attack, "09.HotoMoka");
		Wait(130);
		KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
		Wait(300);
		KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
		KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
		Wait(0);
		SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
	},
}