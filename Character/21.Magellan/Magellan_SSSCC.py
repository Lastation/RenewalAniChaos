Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Probe", CurrentPlayer, "Anywhere", Move, "21. Magellan");      
   },
}



for i = 0, 3, 1 do

radius = (2 * i + 2) / 8 * math.pi;


d = 70;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

d2 = 140;

x2 = math.sin(radius) * d2;
y2 = math.cos(radius) * d2;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer); 
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer); 
      CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Dragoon", "[Skill]Unit_Wait_3", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius = (2 * i + 2) / 8 * math.pi;


d = 70;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

d2 = 140;

x2 = math.sin(radius) * d2;
y2 = math.cos(radius) * d2;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_3", CurrentPlayer); 
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_3", CurrentPlayer); 
      CreateUnit(1, "80 + 1n Artanis", "[Skill]Unit_Wait_3", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "80 + 1n Artanis", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("80 + 1n Artanis", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
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

interval = 50;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
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

interval = 50;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
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

interval = 50;

x = -interval * (math.floor(t / 2));
y = interval * (math.floor(t / 2)) - interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      LMove(178, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


x1 = 150;
y1 = 0;

x2 = 100;
y2 = 50;

x3 = 50;
y3 = 100;


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x1, y1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x1, -y1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y1, x1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y1, -x1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x3, y3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x3, -y3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y3, x3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y3, -x3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(0);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x1 = 150;
y1 = 0;

x2 = 100;
y2 = 50;

x3 = 50;
y3 = 100;

for i = 0, 3, 1 do

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y1, x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y1, -x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
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
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x3, y3);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x3, -y3);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y3, x3);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y3, -x3);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
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