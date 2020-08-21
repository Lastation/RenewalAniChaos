Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      ModifyUnitShields(All, " * Samir Duran", CurrentPlayer, "Anywhere", 100);
      ModifyUnitHitPoints(All, " * Samir Duran", CurrentPlayer, "Anywhere", 100);
   },
}

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -5 * interval, 5 * interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 8, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -9 * interval, -interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -5 * interval, 5 * interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 8, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -9 * interval, -interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -5 * interval, 5 * interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 8, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -9 * interval, -interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(500);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetAllianceStatus(P8, Enemy);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetAllianceStatus(P7, Enemy);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}
