x1 = 75;
y1 = 75;

x2 = 75;
y2 = 0;

x3 = 75;
y3 = -75;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x1, y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x1, -y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y1, x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y1, -x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x2, -y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y2, x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y2, -x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x3, y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x3, -y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y3, x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y3, -x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x1 = 150;
y1 = 75;

x2 = 150;
y2 = 0;

x3 = 150;
y3 = -75;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x1, y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x1, -y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y1, x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y1, -x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x2, -y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y2, x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y2, -x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x3, y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x3, -y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y3, x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y3, -x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
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
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(3, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(3, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      LMove(181, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(200);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, t + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


x1 = 150;
y1 = 75;

x2 = 150;
y2 = 0;

x3 = 150;
y3 = -75;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x1, y1);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x1, -y1);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y1, x1);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y1, -x1);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x2, y2);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x2, -y2);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y2, x2);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y2, -x2);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x3, y3);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x3, -y3);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y3, x3);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y3, -x3);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x1 = 150;
y1 = 75;

x2 = 150;
y2 = 0;

x3 = 150;
y3 = -75;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x1, y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x1, -y1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y1, x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y1, -x1);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x2, -y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y2, x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y2, -x2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x3, y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x3, -y3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y3, x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y3, -x3);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}