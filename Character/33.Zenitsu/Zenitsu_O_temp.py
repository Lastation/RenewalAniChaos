import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   if (v.P_CountMain[playerID] == 0)
   {
      if (v.P_LoopMain[playerID] == 0)
      {
         CreateUnit(1, "Flame Blue", "[Skill]Unit_Wait_8", playerID);  
         SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL");
         MoveLocation(f.location[playerID], f.heroID[playerID], playerID, "Anywhere");
         MoveUnit(All, "Flame Blue", playerID, "Anywhere", f.location[playerID]);
         MoveLocation("33.Zenitsu", "Flame Blue", playerID, "Anywhere");

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;
      }
      else if (v.P_LoopMain[playerID] < 60)
      {      
         var x = 50;

         if (playerID >= 3) x = -x;

         addloc("33.Zenitsu", x * 3, 0);
         MoveUnit(All, "Flame Blue", playerID, "Anywhere", "33.Zenitsu");

         CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", playerID);  
         SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL");

         MoveLocation(f.location[playerID], "Flame Blue", playerID, "Anywhere");
         MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", f.location[playerID]);
         addloc(f.location[playerID], -x, 0);
         MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", f.location[playerID]);
         addloc(f.location[playerID], -x, 0);
         MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", f.location[playerID]);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

         if ((playerID >= 3 && (Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop7") || Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal7")))
            || (playerID < 3 && (Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop8") || Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal8"))))
         {
            SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime");
            RemoveUnitAt(All, "Flame Blue", "Anywhere", playerID);

            trg.Main_Wait(80);

            v.P_CountMain[playerID] = 2;
            v.P_LoopMain[playerID] = 0;
         }
         else if (playerID < 3)
         {
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");

            if (cp < 3)
            {
               if (Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
               }
               else if (Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
               }
               else if (Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
               }

            }
         
            if (Bring(P8, AtLeast, 1, "Buildings", "33.Zenitsu"))
            {
               RemoveUnitAt(All, "Flame Blue", "Anywhere", playerID);

               s.CharacterVoice(3);

               trg.Main_Wait(80);

               v.P_CountMain[playerID] += 1;
               v.P_LoopMain[playerID] = 0;
            }
            else
            {
               trg.Main_Wait(80);

               v.P_LoopMain[playerID] += 1;
            }
         }
         else if (playerID >= 3)
         {
            if (Bring(P7, AtLeast, 1, "Buildings", "33.Zenitsu"))
            {
               RemoveUnitAt(All, "Flame Blue", "Anywhere", playerID);

               s.CharacterVoice(3); 

               trg.Main_Wait(80);

               v.P_CountMain[playerID] += 1;
               v.P_LoopMain[playerID] = 0;
            }
            else
            {
               trg.Main_Wait(80);

               v.P_LoopMain[playerID] += 1;
            }
         }
      }
      else if (v.P_LoopMain[playerID] == 60)
      {      
         SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime");

         trg.Main_Wait(80);
         
         v.P_CountMain[playerID] = 2;
         v.P_LoopMain[playerID] = 0;
      }
   }
   else if (v.P_CountMain[playerID] == 1)
   {
      if (v.P_LoopMain[playerID] < 18)
      {      
         f.DotShape(playerID, 8, "40 + 1n Zealot", 0, 0);
         f.DotShape(playerID, 1, "40 + 1n Guardian", 0, 0);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
      }
      else if (v.P_LoopMain[playerID] == 40)
      {      
         MoveLocation("33.Zenitsu", "Flame Blue", playerID, "Anywhere");

         if (Deaths(CurrentPlayer, Exactly, 0, (210)))
         {
            MoveUnit(All, f.heroID[playerID], playerID, "Anywhere", "33.Zenitsu");
            CenterView("33.Zenitsu");
         }

         f.NxNSquareShape(playerID, 1, "130 + 1n Norad", 3, 75);
         f.DotShape(playerID, 16, "80 + 1n Goliath", 0, 0);
         Order("130 + 1n Norad", playerID, "Anywhere", Attack, "Anywhere");
         MoveUnit(All, "80 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", f.location[playerID]);
         Order("80 + 1n Goliath", playerID, "Anywhere", Attack, "Anywhere");
         SetSwitch("Recall - Milim", Clear);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;
      }
      else if (v.P_LoopMain[playerID] < 45)
      {      
         var i = v.P_LoopMain[playerID] - 41;

         f.EdgeShape(playerID, 1, "60 + 1n Siege", 0, 5 + 2 * i, 100 + 50 * i);
         f.EdgeShape(playerID, 1, "50 + 1n Battlecruiser", 0, 3 + 2 * i, 50 + 50 * i);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;
      }
      else if (v.P_LoopMain[playerID] == 45)
      {      
         KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
         KillUnitAt(All, "80 + 1n Goliath", "Anywhere", playerID);

         f.EdgeShape(playerID, 1, " Unit. Hoffnung 25000", 0, 3, 50);
         f.EdgeShape(playerID, 1, " Unit. Hoffnung 25000", 0, 5, 100);
         f.EdgeShape(playerID, 1, " Unit. Hoffnung 25000", 0, 7, 150);
         f.EdgeShape(playerID, 1, " Unit. Hoffnung 25000", 0, 9, 150);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;
      }

      trg.Main_Wait(80);

      v.P_LoopMain[playerID] += 1;

      else if (v.P_LoopMain[playerID] == 46)
      {     
         s.CharacterVoice(4); 

         v.P_CountMain[playerID] += 1;
         v.P_LoopMain[playerID] = 0;
      }
   }
   else if (v.P_CountMain[playerID] == 2)
   {
      SetDeaths(playerID, SetTo, 1440, " `UniqueCoolTime");

      f.SkillEnd(playerID);
   }

}
