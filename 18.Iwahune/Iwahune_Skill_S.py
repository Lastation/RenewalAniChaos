interval = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(9, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
         intransit = false,
         hallucinated = true,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, - interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, - interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(4, "80 + 1n Artanis", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
         intransit = false,
         hallucinated = true,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      }); 
      CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, - interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(120);
      KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 18, " `SkillWait");
   },
}