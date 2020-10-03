Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 5, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveUnit(All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Probe", CurrentPlayer, "Anywhere", Move, "21. Magellan");   
      ModifyUnitShields(All, " * Probe", CurrentPlayer, "Anywhere", 1);
   },
}

Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      ModifyUnitHangarCount(1, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}



Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      Wait(3200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "60 + 1n Danimoth", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Protoss Interceptor", CurrentPlayer, "Anywhere");
      MoveUnit(4, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("Kakaru (Twilight)", CurrentPlayer, "Anywhere", Move, "21. Magellan");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "21. Magellan");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Move, "21. Magellan");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Move, "21. Magellan");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Move, "21. Magellan");
      KillUnitAt(All, "Any unit", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 3, " `SkillLoop2");
   },
}

Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : Ultimate
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      GiveUnits(All, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P7);
      GiveUnits(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", P7);
      GiveUnits(All, "40 + 1n Wraith", CurrentPlayer, "Anywhere", P7);
      GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P7);
      GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "Kakaru (Twilight)", P7, "Anywhere", P12);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      GiveUnits(All, "40 + 1n Wraith", P7, "Anywhere", P12);
      GiveUnits(All, "50 + 1n Battlecruiser", P7, "Anywhere", P12);
      GiveUnits(All, "60 + 1n Danimoth", P7, "Anywhere", P12);
      Wait(2000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}



Trigger { -- Skill : Ultimate
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      GiveUnits(All, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P8);
      GiveUnits(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", P8);
      GiveUnits(All, "40 + 1n Wraith", CurrentPlayer, "Anywhere", P8);
      GiveUnits(All, "50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", P8);
      GiveUnits(All, "60 + 1n Danimoth", CurrentPlayer, "Anywhere", P8);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "Kakaru (Twilight)", P8, "Anywhere", P12);
      GiveUnits(All, "40 + 1n Mojo", P8, "Anywhere", P12);
      GiveUnits(All, "40 + 1n Wraith", P8, "Anywhere", P12);
      GiveUnits(All, "50 + 1n Battlecruiser", P8, "Anywhere", P12);
      GiveUnits(All, "60 + 1n Danimoth", P8, "Anywhere", P12);
      Wait(2000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(AllPlayers, SetTo, 21001, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      GiveUnits(All, "Kakaru (Twilight)", P12, "Anywhere", CurrentPlayer);
      GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", CurrentPlayer);
      GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", CurrentPlayer);
      GiveUnits(All, "50 + 1n Battlecruiser", P12, "Anywhere", CurrentPlayer);
      GiveUnits(All, "60 + 1n Danimoth", P12, "Anywhere", CurrentPlayer);
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(7000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n High Templar", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "100 + 1n Dragoon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "80 + 1n Tank", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "60 + 3n Siege", "[Skill]Unit_Wait_2", CurrentPlayer); 
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("100 + 1n Dragoon", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("80 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "Any unit", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 330, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
      SetSwitch("UiltimateSwitch", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}