
Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
   },
}


Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "80 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch_Bozo");
      KillUnitAt(All, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "20.EmetSelch_Bozo");   
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, " Unit. Hoffnung 25000", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");    
      MoveUnit(All, " Creep. Licht", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");    
   },
}

t = 9;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 9;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}



t = 5;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "Kakaru (Twilight)", P11, "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

for i = 0, 11, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop4");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P11);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop4");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P11);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

for i = 0, 11, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
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
      CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P11);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
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
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      GiveUnits(1, "Kakaru (Twilight)", CurrentPlayer, "Anywhere", P11);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Add, 6, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(3000);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop4");
      Wait(7800);
      GiveUnits(All, "Kakaru (Twilight)", P11, "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
   },
}


t = 9;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 9;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 11, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
      Bring(CurrentPlayer, AtLeast, 1, "Kakaru (Twilight)", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "Flame Red", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Kakaru (Twilight)", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      MoveUnit(1, "Flame Red", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}


for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Disable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, " Creep. Licht", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Disable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 2, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, " Creep. Licht", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Disable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 3, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, " Creep. Licht", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Disable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5 * i + 4, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, " Creep. Licht", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Disable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, " Creep. Licht", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Bring(CurrentPlayer, Exactly, 0, "Zerg Defiler", "Anywhere");
      Bring(CurrentPlayer, AtLeast, 1, "Any unit", "[Skill]Unit_Wait_ALL");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      RemoveUnitAt(All, "Any unit", "[Skill]Unit_Wait_ALL", CurrentPlayer);
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1000);
      SetDeaths(AllPlayers, SetTo, 20001, " `SkillText_Uiltimate");
      Wait(11000);
      SetDeaths(AllPlayers, SetTo, 20002, " `SkillText_Uiltimate");
      Wait(6000);
      CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 12, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 360, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, " Creep. Licht", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Flame Red", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
      Bring(CurrentPlayer, Exactly, 0, " Creep. Licht", "Anywhere");
      Bring(CurrentPlayer, Exactly, 0, " Unit. Hoffnung 25000", "Anywhere");
      Bring(CurrentPlayer, Exactly, 0, "60 + 1n Hydralisk", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
      Bring(CurrentPlayer, Exactly, 0, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", "40 + 1n Mojo", CurrentPlayer, "Anywhere");
      Order(" Creep. Licht", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Order(" Unit. Hoffnung 25000", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Order("60 + 1n Hydralisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 48, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
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