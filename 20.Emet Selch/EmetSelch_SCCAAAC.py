
Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "20.EmetSelch_Bozo");      
   },
}

for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "60 + 1n Siege", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = true,
         intransit = false,
         hallucinated = true,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
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
      MoveLocation("20.EmetSelch", "60 + 1n Siege", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
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


for i = 0, 2, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Drone", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
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
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "40 + 1n Drone", CurrentPlayer, "Anywhere");
      RemoveUnitAt(4, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Lurker", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
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
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}



for i = 0, 23, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "Zerg Defiler", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "Zerg Defiler", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "Zerg Defiler", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
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
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Guardian", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(300);
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}



t = 4;

for i = 0, t - 1, 1 do

interval = 60;

x = 0 - interval * i;
y = -interval * 3 + interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(0);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 4;

for i = 0, t - 1, 1 do

interval = 60;

x = interval * 3 - interval * i;
y = - interval * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(0);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 4;

for i = 0, t - 1, 1 do

interval = 60;

x = interval * i;
y = interval * 3 - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(0);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 4;

for i = 0, t - 1, 1 do

interval = 60;

x = -interval * 3 + interval * i;
y = interval * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, -interval);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(280);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      Wait(800);
      KillUnitAt(All, "40 + 1n Lurker", "Anywhere", CurrentPlayer);
      SetDeaths(AllPlayers, SetTo, 2004, " `SkillText4");
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
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop4");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop4");
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
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(5, "40 + 1n Drone", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Order("40 + 1n Drone", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1400);
      KillUnitAt(All, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
   },
}


t = 7;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop4");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop4");
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
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Drone", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Order("40 + 1n Drone", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(2200);
      KillUnitAt(All, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
   },
}

Trigger { -- Skill : Use Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Bring(CurrentPlayer, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill");
   },
   actions = {
      Comment("Skill : Use Combo");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      Wait(500);
      SetDeaths(AllPlayers, SetTo, 2005, " `SkillText4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 140, " `SkillStep");
      KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
      PreserveTrigger();
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}