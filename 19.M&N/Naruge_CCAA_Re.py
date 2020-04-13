

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - M&N", Set);
      Wait(1800);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}



Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(6000);
      SetDeaths(CurrentPlayer, Add, 2, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("19.M&N_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      GiveUnits(All, "40 + 1n Marine", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Ghost", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, " Creep. Dunkelheit", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Goliath", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Wraith", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Firebat", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Zergling", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, " Creep. Licht", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Drone", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Mutalisk", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Guardian", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Zealot", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 3n Zeratul", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Mojo", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Gantrithor", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Lurker", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "50 + 1n Tank", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "50 + 1n Battlecruiser", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 3n Siege", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Siege", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Hydralisk", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Dragoon", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n High Templar", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Archon", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Danimoth", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 3n Ghost", Allies, "19.M&N_Bozo", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "80 + 1n Goliath", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Vulture", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Marine", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Tom Kazansky", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Tank", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Mutalisk", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Guardian", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Artanis", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Ghost", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "100 + 1n Hyperion", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "100 + 1n Dragoon", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "120 + 1n Archon", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "130 + 1n Norad", Allies, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "130 + 1n Arbiter", Allies, "19.M&N_Bozo", CurrentPlayer);
   },
}

interval = 100;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 -interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(800);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


interval = 100;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 -interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      Wait(600);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, " Unit. Schnee", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(7, " Unit. Schnee", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
   },
}
interval = 75;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 -interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, AtMost, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop2");
      Deaths(CurrentPlayer, AtMost, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

interval = 75;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 -interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      RemoveUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Ghost", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, " Creep. Licht", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 3n Zeratul", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer);
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - M&N", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}