Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 3, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Zerg Queen", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N_Bozo");
      RemoveUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      Order(" * Infested Kerrigan", CurrentPlayer, "Anywhere", Move, "19.M&N_Bozo");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
      Wait(4000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
      Wait(2800);
      CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("19.M&N_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N_Bozo");
      SetDeaths(AllPlayers, SetTo, 1002, " `SkillText4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
      Wait(1500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Mond", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Mond", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Unit. Schnee", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Unit. Schnee", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}


Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Blumen", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Blumen", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Garten", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Garten", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Brunnen", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Brunnen", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Traum", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Traum", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Unit. Polarlicht", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Unit. Polarlicht", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P8, AtLeast, 1, " Struct. Wald", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Wald", P8, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}



Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Mond", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Mond", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Unit. Schnee", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Unit. Schnee", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}


Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Blumen", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Blumen", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Garten", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Garten", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Brunnen", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Brunnen", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Traum", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Traum", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Unit. Polarlicht", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Unit. Polarlicht", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Bring(P7, AtLeast, 1, " Struct. Wald", "19.M&N_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N", " Struct. Wald", P7, "19.M&N_Bozo");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "Anywhere", "19.M&N");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(25, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("Target", CurrentPlayer, "Anywhere", Move, "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "19.M&N", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "19.M&N", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mutalisk", "19.M&N", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 3, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(25, "50 + 1n Tank", "[Skill]Unit_Wait_4", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Zerg Defiler", CurrentPlayer, "Anywhere");
      Order("Target", CurrentPlayer, "Anywhere", Move, "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "19.M&N", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "19.M&N", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mutalisk", "19.M&N", CurrentPlayer);
   },
}



for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 100 + 10 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, AtLeast, 3, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "19.M&N");
   },
}
end

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 100 + 10 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
   },
}
end

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 100 + 10 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Add, 6, " `SkillLoop4");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Add, 4, " `SkillLoop4");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop4");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 40 + 40 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(2, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(2, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(2, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(2, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 40 + 40 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(2, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(2, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(2, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(2, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      Order("80 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(1800);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 40 + 40 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", "Target", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Zerg Defiler", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}