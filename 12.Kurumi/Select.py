
Trigger { -- System : Select
	players = {P1, P2, P3, P4, P5, P6},
	conditions = {
		Bring(P10, AtLeast, 1, " * Sarah Kerrigan", "11.TokisakiKurumi");
		Bring(CurrentPlayer, AtLeast, 1, "Terran Civilian", "11.TokisakiKurumi");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]SkillMove-Use");
	},
	actions = {
		Comment("System : Select");
		KillUnitAt(All, "Protoss Corsair", "[Skill]SkillMove-Use", CurrentPlayer);
		RemoveUnitAt(All, "Terran Civilian", "[Select]Select Unit", CurrentPlayer);
		RemoveUnitAt(1, " * Sarah Kerrigan", "11.TokisakiKurumi", P10);
		CreateUnit(1, " * Sarah Kerrigan", "11.TokisakiKurumi", CurrentPlayer);
		SetDeaths(CurrentPlayer, SetTo, 3000, " * Sarah Kerrigan");
		SetDeaths(CurrentPlayer, SetTo, 10000, " `Property");
		SetDeaths(CurrentPlayer, SetTo, 11, " `HeroNum");
		PreserveTrigger();
	},
}

Trigger { -- System : Bug Founded..
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, Exactly, 0, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 1, " `DeadCount");
	},
	actions = {
		Comment("System : Bug Founded..");
		PreserveTrigger();
		CreateUnit(1, " * Sarah Kerrigan", "[Select]Select Unit", CurrentPlayer);
	},
}