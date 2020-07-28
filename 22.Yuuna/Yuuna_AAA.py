Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 13, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("22.Yuuna_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");     
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - Yuuna", Set);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      Wait(2200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      Wait(5800);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}


for i = 0, 7, 1 do

d = 200;

radius = i / 8 * math.pi;

y = math.cos(radius) * d;
x = math.sin(radius) * d;
y = math.floor(y + 0.5);
x = math.floor(x + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(16, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(16, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop3");
   },
}

end

for i = 0, 7, 1 do

d = 200;

radius = i / 8 * math.pi;

y = math.cos(radius) * d;
x = math.sin(radius) * d;
y = math.floor(y + 0.5);
x = math.floor(x + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      CreateUnit(16, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(16, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(8, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(8, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(3, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      Wait(500);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


t = 4;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(500);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(5, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(5, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(800);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(500);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(500);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

t = 11;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(9000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(100);
      KillUnitAt(11, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

distance = 250;
interval = 50;

n = 11;

radius_d = (2 * i + 1) / 4 * math.pi;

x_d = math.sin(radius_d) * distance;
y_d = math.cos(radius_d) * distance;
x_d = math.floor(x_d + 0.5);
y_d = math.floor(y_d + 0.5);

radius = (2 * i + 3) / 4 * math.pi;

x_o = math.sin(radius) * (interval * math.floor(n / 2));
y_o = math.cos(radius) * (interval * math.floor(n / 2));
x_o = math.floor(x_o + 0.5);
y_o = math.floor(y_o + 0.5);

x_i = math.sin(radius) * -interval;
y_i = math.cos(radius) * -interval;
x_i = math.floor(x_i + 0.5);
y_i = math.floor(y_i + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(11, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

distance = 300;
interval = 50;

n = 11;

radius_d = (2 * i + 1) / 4 * math.pi;

x_d = math.sin(radius_d) * distance;
y_d = math.cos(radius_d) * distance;
x_d = math.floor(x_d + 0.5);
y_d = math.floor(y_d + 0.5);

radius = (2 * i + 3) / 4 * math.pi;

x_o = math.sin(radius) * (interval * math.floor(n / 2));
y_o = math.cos(radius) * (interval * math.floor(n / 2));
x_o = math.floor(x_o + 0.5);
y_o = math.floor(y_o + 0.5);

x_i = math.sin(radius) * -interval;
y_i = math.cos(radius) * -interval;
x_i = math.floor(x_i + 0.5);
y_i = math.floor(y_i + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(11, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(11, "60 + 3n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      GiveUnits(All, "60 + 3n Siege", CurrentPlayer, "Anywhere", P11);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


for i = 0, 7, 1 do

distance = 100;
interval = 75;

n = 11;

radius_d = (i + 7) / 4 * math.pi;

x_d = math.sin(radius_d) * distance;
y_d = math.cos(radius_d) * distance;
x_d = math.floor(x_d + 0.5);
y_d = math.floor(y_d + 0.5);

radius = (i + 9) / 4 * math.pi;

x_o = math.sin(radius) * (interval * math.floor(n / 2));
y_o = math.cos(radius) * (interval * math.floor(n / 2));
x_o = math.floor(x_o + 0.5);
y_o = math.floor(y_o + 0.5);

x_i = math.sin(radius) * -interval;
y_i = math.cos(radius) * -interval;
x_i = math.floor(x_i + 0.5);
y_i = math.floor(y_i + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      CreateUnit(11, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

end

for i = 0, 7, 1 do

distance = 100;
interval = 75;

n = 11;

radius_d = (i + 3) / 4 * math.pi;

x_d = math.sin(radius_d) * distance;
y_d = math.cos(radius_d) * distance;
x_d = math.floor(x_d + 0.5);
y_d = math.floor(y_d + 0.5);

radius = (i + 5) / 4 * math.pi;

x_o = math.sin(radius) * (interval * math.floor(n / 2));
y_o = math.cos(radius) * (interval * math.floor(n / 2));
x_o = math.floor(x_o + 0.5);
y_o = math.floor(y_o + 0.5);

x_i = math.sin(radius) * -interval;
y_i = math.cos(radius) * -interval;
x_i = math.floor(x_i + 0.5);
y_i = math.floor(y_i + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(11, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

end

for i = 0, 7, 1 do

distance = 100;
interval = 75;

n = 11;

radius_d = (i) / 4 * math.pi;

x_d = math.sin(radius_d) * distance;
y_d = math.cos(radius_d) * distance;
x_d = math.floor(x_d + 0.5);
y_d = math.floor(y_d + 0.5);

radius = (i + 2) / 4 * math.pi;

x_o = math.sin(radius) * (interval * math.floor(n / 2));
y_o = math.cos(radius) * (interval * math.floor(n / 2));
x_o = math.floor(x_o + 0.5);
y_o = math.floor(y_o + 0.5);

x_i = math.sin(radius) * -interval;
y_i = math.cos(radius) * -interval;
x_i = math.floor(x_i + 0.5);
y_i = math.floor(y_i + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(11, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x_d + x_o, y_d + y_o);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, x_i, y_i);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 3, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 4, " `SkillLoop3");
   },
}

end



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 9, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 8, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      GiveUnits(All, "60 + 3n Siege", P11, "Anywhere", CurrentPlayer);
      Wait(4200);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}


for j = 0, 3, 1 do

t = 9;

for i = 0, t - 1, 1 do

interval = 75;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, (2 * i) + 19 * j, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "80 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, (2 * i + 1) + 19 * j, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(2, "80 + 1n Goliath", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, (t * 2) + 19 * j, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "80 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("80 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(0);
      KillUnitAt(All, "80 + 1n Goliath", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 76, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Use Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, AtLeast, 350, " `UltimateCoolTime");
      Bring(CurrentPlayer, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill");
   },
   actions = {
      Comment("Skill : Use Ultimate");
      SetDeaths(AllPlayers, SetTo, 22010, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 320, " `SkillStep");
      SetDeaths(CurrentPlayer, Subtract, 350, " `UltimateCoolTime");
      SetSwitch("UiltimateSwitch", Set);
      KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
      PreserveTrigger();
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      SetSwitch("Recall - Yuuna", Clear);
      SetSwitch("UiltimateSwitch", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}