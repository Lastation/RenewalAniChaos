Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 13, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Devouring One", CurrentPlayer, "Anywhere", Move, "22.Yuuna_Bozo");      
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 3;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(3, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(1, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(460);
      SetSwitch("Recall - Yuuna", Set);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

x = 0 + 50 * i;
y = 50 * 4 - 50 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop3");
   },
}

x = 50 * 4 - 50 * i;
y = 0 - 50 * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 4, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop3");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 6, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1500);
      SetDeaths(AllPlayers, SetTo, 4001, " `SkillText4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 6, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "22.Yuuna_Bozo");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Move, "22.Yuuna_Bozo");
   },
}


for i = 0, 1, 1 do

d = 50;
interval = 50;

radius = (8 * i + 5) / 10 * math.pi;
radius_i1 = ((8 * i + 5) / 10 + (1 / 8)) * math.pi;
radius_i2 = ((8 * i + 5) / 10 - (1 / 8)) * math.pi;

y_o = math.cos(radius) * d;
y_o = math.floor(y_o + 0.5);

x_o = math.sin(radius) * d;
x_o = math.floor(x_o + 0.5);

y_i1 = math.cos(radius_i1) * interval;
y_i1 = math.floor(y_i1 + 0.5);

y_i2 = math.cos(radius_i2) * interval;
y_i2 = math.floor(y_i2 + 0.5);

x_i1 = math.sin(radius_i1) * interval;
x_i1 = math.floor(x_i1 + 0.5);

x_i2 = math.sin(radius_i2) * interval;
x_i2 = math.floor(x_i2 + 0.5);



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(3, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


d = 50;
interval = 50;

radius = (17) / 10 * math.pi;
radius_i1 = ((17) / 10 + (1 / 8)) * math.pi;
radius_i2 = ((17) / 10 - (1 / 8)) * math.pi;

y_o = math.cos(radius) * d;
y_o = math.floor(y_o + 0.5);

x_o = math.sin(radius) * d;
x_o = math.floor(x_o + 0.5);

y_i1 = math.cos(radius_i1) * interval;
y_i1 = math.floor(y_i1 + 0.5);

y_i2 = math.cos(radius_i2) * interval;
y_i2 = math.floor(y_i2 + 0.5);

x_i1 = math.sin(radius_i1) * interval;
x_i1 = math.floor(x_i1 + 0.5);

x_i2 = math.sin(radius_i2) * interval;
x_i2 = math.floor(x_i2 + 0.5);



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(3, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P12);
      Wait(1200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 1, 1 do

d = 50;
interval = 50;

radius = (8 * i + 1) / 10 * math.pi;
radius_i1 = ((8 * i + 1) / 10 + (1 / 8)) * math.pi;
radius_i2 = ((8 * i + 1) / 10 - (1 / 8)) * math.pi;

y_o = math.cos(radius) * d;
y_o = math.floor(y_o + 0.5);

x_o = math.sin(radius) * d;
x_o = math.floor(x_o + 0.5);

y_i1 = math.cos(radius_i1) * interval;
y_i1 = math.floor(y_i1 + 0.5);

y_i2 = math.cos(radius_i2) * interval;
y_i2 = math.floor(y_i2 + 0.5);

x_i1 = math.sin(radius_i1) * interval;
x_i1 = math.floor(x_i1 + 0.5);

x_i2 = math.sin(radius_i2) * interval;
x_i2 = math.floor(x_i2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(5, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(5, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(3, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
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
      CreateUnit(3, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_o, y_o);
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i2, y_i2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i1, y_i1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P12);
      Wait(1600);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      Wait(550);
      SetDeaths(AllPlayers, SetTo, 4002, " `SkillText4");
      GiveUnits(All, "60 + 1n Siege", P12, "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      KillUnitAt(4, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Mutalisk", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      KillUnitAt(4, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
   },
}

interval = 50;

x = - interval * 4;
y = interval * 2;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = - interval * 4;
y = interval * 6;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Wait(0);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x = interval * 4;
y = interval * 6;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = - interval * 4;
y = interval * 2;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Wait(0);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = interval * 4;
y = interval * 2;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      CreateUnit(9, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x = interval * 4;
y = interval * 6;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = - interval * 4;
y = interval * 6;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, -interval);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = interval * 4;
y = interval * 2;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, -interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 5, 1 do

x = 225 - 75 * i;
y = 150 - 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


for i = 0, 5, 1 do

x = 150 - 75 * i;
y = -225 + 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 14, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 5, 1 do

x = 225 - 75 * i;
y = 150 - 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 21, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


for i = 0, 5, 1 do

x = 150 - 75 * i;
y = -225 + 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 27, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 33, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

t = 3;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 34, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(3, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 34, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(320);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(2300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 35, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}


for i = 0, 11, 1 do

radius = i / 32 * math.pi;

d = 150 - 5 * i;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(32, "Rhynadon (Badlands)", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(8, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(8, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(8, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(8, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(5, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


t = 5;

for i = 0, t - 1, 1 do

interval = 100;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(5, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(2200);
      KillUnitAt(5, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(5, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(5, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(5, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(5, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 14, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetSwitch("Recall - Yuuna", Clear);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}