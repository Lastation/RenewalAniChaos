Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      ModifyUnitShields(All, " * Sarah Kerrigan", CurrentPlayer, "Anywhere", 1);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Sarah Kerrigan", CurrentPlayer, "Anywhere", Move, "16.Seraphim_Bozo");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(5000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(1000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(6000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(1000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(8000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(1000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(6500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(1000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(24000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16021, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16022, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16023, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16024, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16031, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16032, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16033, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16034, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16041, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16042, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16043, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16044, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16045, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16046, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16051, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16052, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16053, " `SkillText_Unique");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 16054, " `SkillText_Unique");
   },
}


Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - Seraphim", Clear);
      SetDeaths(P1, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(P2, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(P3, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(CurrentPlayer, SetTo, 0, " `UltimateCoolTime");
      KillUnitAt(All, " * Sarah Kerrigan", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " * Sarah Kerrigan");
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");

   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 400, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - Seraphim", Clear);
      SetDeaths(P4, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(P5, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(P6, SetTo, 1000, " `UltimateCoolTime");
      SetDeaths(CurrentPlayer, SetTo, 0, " `UltimateCoolTime");
      KillUnitAt(All, " * Sarah Kerrigan", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " * Sarah Kerrigan");
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");

   },
}