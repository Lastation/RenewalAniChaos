import variable as v;
import func.trig as trg;
import func.sound as s;

function main(playerID)
{
   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] < 4)
         {         

            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 2 * v.P_LoopMain[playerID] + 1, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Main_Wait(80);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 6, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Goliath", 3, 50);
            Order("40 + 1n Goliath", playerID, "Anywhere", Attack, "Anywhere");

            trg.Main_Wait(80);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 5)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 114, 114);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 114, 190);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 190, 114);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 190, 190);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 38, 114);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 38, 175);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 114, 38);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 175, 38);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 114, 114);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 114, 190);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 190, 114);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 190, 190);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 38, 114);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 38, 175);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 114, 38);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 175, 38);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            trg.Main_Wait(720);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }

      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0)
         {         
            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 3, 50);
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Goliath", 3, 50);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID); 
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);

            trg.Main_Wait(320);

            v.P_LoopMain[playerID] += 1;


         }
         else if (v.P_LoopMain[playerID] == 1)
         {         
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 0);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 50);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 100);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 150);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 200);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 0);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 50);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 100);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 150);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 200);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 200, 0);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 200, 50);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 200, 100);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 200, 150);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 200, 200);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 100);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 150);
            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 200);
            trg.Shape_Edge(playerID, 1, "40 + 1n Goliath", 45, 3, 125);
            trg.Shape_Edge(playerID, 1, "40 + 1n Goliath", 45, 5, 175);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);

            trg.Main_Wait(320);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }

         
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID); 

            s.CharacterVoice(4);
         }

         if (v.P_LoopMain[playerID] < 8)
         {         
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.MoveLoc(v.P_UnitID[playerID], playerID, 200 - 50 * (v.P_LoopMain[playerID] % 4), 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "50 + 1n Tank");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, -200 + 50 * (v.P_LoopMain[playerID] % 4), -50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "50 + 1n Tank");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, 50 * (v.P_LoopMain[playerID] % 4), -200 + 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, -50 * (v.P_LoopMain[playerID] % 4), 200 - 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Main_Wait(160);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Main_Wait(80);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         if (v.P_LoopMain[playerID] == 0)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Main_Wait(240);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 1)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 200);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Main_Wait(240);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
         
      }
      else if (v.P_CountMain[playerID] == 4)
      {

         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         trg.SkillEnd();


      }


   }
}