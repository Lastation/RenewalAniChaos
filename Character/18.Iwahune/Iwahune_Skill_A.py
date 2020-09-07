x1 = 50;
y1 = 50;

x2 = 50;
y2 = 0;

x3 = 100;
y3 = 0;

for i = 0, 3, 1 do

Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      LMove(170, x1, y1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y1, x1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y1, -x1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      LMove(170, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y2, x2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y2, -x2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      LMove(170, x3, y3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x3, -y3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y3, x3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y3, -x3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y1, x1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y1, -x1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y2, x2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y2, -x2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x3, y3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x3, -y3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y3, x3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y3, -x3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 15, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y1, x1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y1, -x1);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y2, x2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y2, -x2);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnitWithProperties(4, " Creep. Dunkelheit", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
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
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x3, y3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x3, -y3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y3, x3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y3, -x3);
      MoveUnit(1, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order(" Creep. Dunkelheit", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(150);
      KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : C
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}