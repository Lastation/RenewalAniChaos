Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 4, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveUnit(All, "80 + 1n Artanis", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, "80 + 1n Marine", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Probe", CurrentPlayer, "Anywhere", Move, "21. Magellan");      
   },
}


for i = 0, 1, 1 do

x = 100 - 50 * i;
y = 0;

x2 = 75 - 50 * i;
y2 = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

x = 50;
y = 50;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x = 125;
y = 0;

x2 = 80;
y2 = 80;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "80 + 1n Marine", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnitWithProperties(8, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "80 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      Wait(400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(56, " Unit. Schnee", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(7, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 4, " `SkillLoop2");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
   },
}

for i = 0, 3, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "Zerg Queen", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(2, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "Zerg Queen", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(2, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(0);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


x = 125;
y = 0;

x2 = 80;
y2 = 80;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(8, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "Zerg Queen", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(2, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "Zerg Queen", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(2, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      Order("80 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(0);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}