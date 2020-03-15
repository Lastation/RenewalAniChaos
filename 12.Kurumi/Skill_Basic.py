x = 64;
y = 64;

Trigger { -- Skill : A
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 3000, " * Sarah Kerrigan");
		Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
	},
	actions = {
		Comment("Skill : A");
		PreserveTrigger();
		CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
		CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
		SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
		MoveLocation("09.HotoMoka", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		LMove(153, x, y);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		LMove(153, -y, x);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		LMove(153, -x, -y);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		LMove(153, y, -x);
		MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "09.HotoMoka");
		MoveLocation("09.HotoMoka", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
		KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
		RemoveUnitAt(All, "men", "[Skill]Unit_Wait_ALL", CurrentPlayer);
		SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
	},
}
