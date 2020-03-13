
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `UniqueSkill");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillStep");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 8, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
		ModifyUnitShields(All, " * Samir Duran", CurrentPlayer, "Anywhere", 1);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop4");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 900, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 800, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 700, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 600, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 500, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 400, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 7, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 300, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 8, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillStep");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 200, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 10, " `SkillStep");
 },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillStep");
   },
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 900, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14000, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 848, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14001, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 2, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 806, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 800, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 1, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 806, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 2, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 800, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14002, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 2, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 763, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14003, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 3, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 722, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 700, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 2, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 722, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 3, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 700, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14004, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 4, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 661, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 600, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 3, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 661, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 4, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 600, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14005, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 5, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 534, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 500, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 4, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 534, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 5, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 500, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14006, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 6, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 442, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 400, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 5, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 442, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 6, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 400, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14007, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 7, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 345, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 300, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 6, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 345, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 7, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 300, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14008, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 8, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 246, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 200, " `SkillLoop4");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtMost, 7, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 246, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}


Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 8, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 200, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(AllPlayers, SetTo, 14009, " `SkillText_Unique");
	},
}

Trigger { -- Skill : S
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, AtLeast, 8, " `UniqueSkill");
		Deaths(CurrentPlayer, Exactly, 179, " `SkillLoop4");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
	},
}


interval = 32;


x = - interval * 8;
y = 0;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
		SetSwitch("Recall - Yashiro", Set);
      CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(164, x, y);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
   },
}

x = 0;
y = interval * 8;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(164, x, y);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, -interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
   },
}



x = 0;
y = - interval * 8;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_7", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(164, x, y);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
   },
}


x = interval * 8;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(9, "Bengalaas (Jungle)", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(164, x, y);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      LMove(164, -interval, interval);
      MoveUnit(1, "Bengalaas (Jungle)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", CurrentPlayer);
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Switch("Recall - Yashiro", Set)
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
		SetSwitch("Recall - Yashiro", Clear);
   },
}