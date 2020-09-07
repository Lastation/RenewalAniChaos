Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveUnit(All, "100 + 1n Dragoon", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      MoveLocation("16.Seraphim_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      ModifyUnitShields(All, " * Sarah Kerrigan", CurrentPlayer, "Anywhere", 1);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Sarah Kerrigan", CurrentPlayer, "Anywhere", Move, "16.Seraphim_Bozo");
   },
}

interval = 50;

for i = 0, 7, 1 do

d = 50 + i * 50;

x = d;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnitWithProperties(4, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y + 2 * interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnitWithProperties(4, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x + 2 * interval, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnitWithProperties(4, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y + 2 * interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 3, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(5, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnitWithProperties(4, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x + 2 * interval, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 40, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

x = 400 - 50 * i;
y = 50 * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");   
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Move, "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Add, 3, " `SkillLoop3");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(5500);
      SetDeaths(AllPlayers, SetTo, 16001, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "80 + 1n Artanis", P7, "Anywhere", P12);
      Wait(1500);
      GiveUnits(All, "80 + 1n Artanis", P12, "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P12);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P8);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "80 + 1n Artanis", P8, "Anywhere", P12);
      Wait(1500);
      GiveUnits(All, "80 + 1n Artanis", P12, "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      GiveUnits(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", P12);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "100 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      RemoveUnitAt(All, "100 + 1n Dragoon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
      Bring(CurrentPlayer, Exactly, 0, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      RemoveUnitAt(All, "100 + 1n Dragoon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Bring(P12, AtLeast, 1, "80 + 1n Artanis", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "120 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", "80 + 1n Artanis", P12, "Anywhere");
      GiveUnits(1, "80 + 1n Artanis", P12, "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "120 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      RemoveUnitAt(All, "60 + 1n High Templar", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Archon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
      Bring(P12, Exactly, 0, "80 + 1n Artanis", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(All, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      RemoveUnitAt(All, "60 + 1n High Templar", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Archon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(4000);
      KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      SetSwitch("UiltimateSwitch", Clear);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");

   },
}