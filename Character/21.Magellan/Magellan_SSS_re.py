
x = 50;
y = 50;

for i = 0, 3, 1 do

radius = (2 * i + 1) / 4 * math.pi;


d = 140;

x2 = math.sin(radius) * d;
y2 = math.cos(radius) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer); 
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer); 
      CreateUnit(1, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "130 + 1n Arbiter", "[Skill]Unit_Wait_8", CurrentPlayer);  
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
      LMove(178, -y, x);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "130 + 1n Arbiter", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 1, 1 do

x = 100 - 50 * i;
y = 0;

x2 = 75 - 50 * i;
y2 = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
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
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


x = 50;
y = 50;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(4, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x1 = 50;
y1 = 0;

x2 = 100;
y2 = 0;

x3 = 50;
y3 = 50;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x1, y1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x1, -y1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y1, x1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y1, -x1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x3, y3);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x3, -y3);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y3, x3);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y3, -x3);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x1 = 50;
y1 = 0;

x2 = 100;
y2 = 0;

x3 = 50;
y3 = 50;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
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
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
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
      Wait(200);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x1 = 50;
y1 = 0;

x2 = 100;
y2 = 0;

x3 = 50;
y3 = 50;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x1, y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x1, -y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y1, x1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y1, -x1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x2, y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x2, -y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y2, x2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y2, -x2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_2", CurrentPlayer); 
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x3, y3);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x3, -y3);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y3, x3);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y3, -x3);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
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