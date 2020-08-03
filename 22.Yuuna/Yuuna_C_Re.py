import Function as f;

const s = StringBuffer();

function main(cp, location, heroID)
{
   f.loop[cp] = dwread_epd(212 * 12 + cp);
   f.count[cp]  = dwread_epd(181 * 12 + cp);

   if (Deaths(cp, Exactly, 0, " `WaitTime"))
   {
      if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {                        
            f.SquareShape(heroID, 1, "60 + 1n Archon", location, cp, 200 - f.loop[cp] * 50, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            
            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(heroID, 4, "60 + 1n Archon", location, cp, 50, 50);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 5)
         {
            f.NxNSquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 0);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }

      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {         
            f.distance[cp] = 125;
            
            f.Table_Cos(cp, 45 + 90 * f.loop[cp], f.distance[cp]);
            f.Table_Sin(cp, 45 + 90 * f.loop[cp], f.distance[cp]);

            f.MoveLoc(heroID, location, cp, f.CosAngle[cp], f.SinAngle[cp]);
            f.SkillUnit(1, "40 + 1n Wraith", location, cp);
            f.SkillUnit(1, "40 + 1n Goliath", location, cp);

            f.distance[cp] = 175;

            f.Table_Cos(cp, 45 + 90 * f.loop[cp], f.distance[cp]);
            f.Table_Sin(cp, 45 + 90 * f.loop[cp], f.distance[cp]);

            f.MoveLoc(heroID, location, cp, f.CosAngle[cp], f.SinAngle[cp]);
            f.SkillUnit(1, "40 + 1n Wraith", location, cp);
            f.SkillUnit(1, "40 + 1n Goliath", location, cp);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 4)
         {
            MoveLocation(location, heroID, cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, location);

            f.SkillWait(cp, 0);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 4)
         {         
            f.distance[cp] = 100;
            
            f.Table_Cos(cp, 0 + 90 * f.loop[cp], f.distance[cp]);
            f.Table_Sin(cp, 0 + 90 * f.loop[cp], f.distance[cp]);

            f.MoveLoc(heroID, location, cp, f.CosAngle[cp], f.SinAngle[cp]);
            f.SkillUnit(1, "40 + 1n Wraith", location, cp);
            f.SkillUnit(1, "40 + 1n Goliath", location, cp);

            f.distance[cp] = 150;

            f.Table_Cos(cp, 0 + 90 * f.loop[cp], f.distance[cp]);
            f.Table_Sin(cp, 0 + 90 * f.loop[cp], f.distance[cp]);

            f.MoveLoc(heroID, location, cp, f.CosAngle[cp], f.SinAngle[cp]);
            f.SkillUnit(1, "40 + 1n Wraith", location, cp);
            f.SkillUnit(1, "40 + 1n Goliath", location, cp);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 4)
         {
            MoveLocation(location, heroID, cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, location);

            f.SkillWait(cp, 50);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}