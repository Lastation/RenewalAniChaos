
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, Add, 60, " `SkillLoop2");
   },
}

for i = 0, 7, 1 do

radius = i / 8 * math.pi;

d = 150;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(2, "Zerg Defiler", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "Zerg Defiler", "Anywhere", P10);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      Wait(90);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 60, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop3");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 30, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 2, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 30, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      SetDeaths(AllPlayers, SetTo, 2003, " `SkillText3");
      PreserveTrigger();
   },
}


interval = 36;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - interval, - interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, - interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - 2 * interval, 0);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, - 2 * interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 2 * interval, 0);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - interval, - interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, - interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - 2 * interval, 0);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, - 2 * interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 2 * interval, 0);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      GiveUnits(All, "Zerg Defiler", P10, "Anywhere", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - interval, - interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, - interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - interval, - interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, - interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      GiveUnits(All, "Zerg Defiler", P10, "Anywhere", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - 2 * interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, - 2 * interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 2 * interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "Zerg Defiler", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Zerg Defiler", CurrentPlayer, "Anywhere", P10);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, - 2 * interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, - 2 * interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 2 * interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 10, " `SkillLoop3");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "Zerg Defiler", "Anywhere", P10);
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}