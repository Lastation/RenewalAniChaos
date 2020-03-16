radius1 = 1 / 4 * math.pi;
radius2 = math.pi;

d = 75;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 100;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 100;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 125;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnitWithProperties(8, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}