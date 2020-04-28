
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 2, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("19.M&N_Bozo2", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      ModifyUnitShields(All, " * Infested Kerrigan", CurrentPlayer, "Anywhere", 100);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
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
   players = {Force1, Force2},
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
      Wait(4000);
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
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("19.M&N_Bozo", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      GiveUnits(All, "40 + 1n Marine", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Ghost", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, " Creep. Dunkelheit", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Goliath", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Wraith", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Firebat", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Zergling", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, " Creep. Licht", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Drone", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Mutalisk", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Guardian", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Zealot", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 3n Zeratul", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Mojo", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Gantrithor", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "40 + 1n Lurker", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "50 + 1n Tank", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "50 + 1n Battlecruiser", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 3n Siege", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Siege", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Hydralisk", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Dragoon", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n High Templar", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Archon", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 1n Danimoth", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "60 + 3n Ghost", Foes, "19.M&N_Bozo", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "80 + 1n Goliath", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Vulture", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Marine", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Tom Kazansky", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Tank", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Mutalisk", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Guardian", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Artanis", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "80 + 1n Ghost", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "100 + 1n Hyperion", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "100 + 1n Dragoon", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "120 + 1n Archon", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "130 + 1n Norad", Foes, "19.M&N_Bozo", CurrentPlayer);
      GiveUnits(All, "130 + 1n Arbiter", Foes, "19.M&N_Bozo", CurrentPlayer);
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - M&N", Clear);
      SetDeaths(AllPlayers, SetTo, 19001, " `SkillText_Uiltimate");
      Wait(2000);
      SetDeaths(AllPlayers, SetTo, 19002, " `SkillText_Uiltimate");
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
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "40 + 3n Zeratul", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, interval, 0);
      MoveUnit(1, "40 + 3n Zeratul", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      RemoveUnitAt(All, "40 + 3n Zeratul", "[Skill]Unit_Wait_ALL", CurrentPlayer);
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
      Bring(CurrentPlayer, AtLeast, 1, "40 + 3n Zeratul", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
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
      KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Marine", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Ghost", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "120 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
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
      KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Ghost", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Creep. Licht", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Zealot", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer);
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
      SetSwitch("UiltimateSwitch", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}