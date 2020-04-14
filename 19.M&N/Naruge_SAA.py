Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
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

for i = 0, 1, 1 do

x = 50;
y = 50;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Artanis", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x = 100;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

x = 150;
y = 150;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 3, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

for i = 0, 3, 1 do

interval = 50;

x1 = 4 * interval - interval * i;
y1 = 4 * interval - (interval + interval * i);

x2 = 4 * interval - (interval + interval * i);
y2 = 4 * interval - interval * i;

x3 = 4 * interval - interval * i;
y3 = 4 * interval - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(8, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      Wait(0);   
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

for i = 0, 3, 1 do

interval = 50;

x1 = interval + interval * i;
y1 = interval / 2;

x2 = interval + interval * i;
y2 = -interval / 2;

x3 = interval + interval * i;
y3 = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(8, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
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
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(400);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(900);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


x = 60;
y = 60;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

x1 = 100;
y1 = 100;

x1 = 150;
y1 = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 3, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

for i = 0, 1, 1 do

interval = 50;

x1 = interval * i;
y1 = (interval + interval * i);

x2 = (interval + interval * i);
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

interval = 50;

x1 = interval * i;
y1 = (interval + interval * i);

x2 = (interval + interval * i);
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 1, 1 do

interval = 50;

x1 = interval * i;
y1 = (interval + interval * i);

x2 = (interval + interval * i);
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

interval = 50;

x1 = interval * i;
y1 = (interval + interval * i);

x2 = (interval + interval * i);
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

for i = 0, 2, 1 do

x = -interval * 1;
y = interval * 1 -interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(250);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1200);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


x = 60;
y = 60;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

x1 = 100;
y1 = 100;

x1 = 150;
y1 = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


x = 100;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(36, "40 + 1n Zealot", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(9, "40 + 1n Zealot", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

x = 150;
y = 150;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 3, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}


for i = 0, 3, 1 do

interval = 50;

x1 = 4 * interval - interval * i;
y1 = 4 * interval - (interval + interval * i);

x2 = 4 * interval - (interval + interval * i);
y2 = 4 * interval - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      Wait(0);   
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

for i = 0, 3, 1 do

interval = 50;

x1 = 4 * interval - interval * i;
y1 = 4 * interval - (interval + interval * i);

x2 = 4 * interval - (interval + interval * i);
y2 = 4 * interval - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(200);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

interval = 50;

x1 = 4 * interval - interval * i;
y1 = 4 * interval - (interval + interval * i);

x2 = 4 * interval - (interval + interval * i);
y2 = 4 * interval - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}