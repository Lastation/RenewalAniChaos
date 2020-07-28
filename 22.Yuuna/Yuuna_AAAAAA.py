Trigger { -- Skill : Ultimate
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 13, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("22.Yuuna_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");     
   },
}
Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 12, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
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

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - Yuuna", Set);
      Wait(2000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 24, 1 do

radius = i / 32 * math.pi;

d = 50 + 8 * i;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(32, "Rhynadon (Badlands)", "[Skill]Unit_Wait_7", CurrentPlayer);
      CreateUnit(32, "Rhynadon (Badlands)", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(16, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(16, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(16, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(16, "Rhynadon (Badlands)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1300);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "60 + 1n Siege", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      GiveUnits(All, "60 + 1n Siege", CurrentPlayer, "Anywhere", P11);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1200);
      GiveUnits(All, "60 + 1n Siege", P11, "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop2");
      Wait(1400);
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(0);
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(0);
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
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
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(2, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(2, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(0);
      RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(7, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
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
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t * 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(3500);
      Wait(14400);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetSwitch("Recall - Yuuna", Clear);
      SetSwitch("UiltimateSwitch", Clear);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}