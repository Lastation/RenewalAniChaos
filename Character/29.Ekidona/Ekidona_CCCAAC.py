import variable as v;
import func.trig as trg;
import func.trigadv as adv;
import func.trigepic as epic;
import func.sound as s;

function NxNSquareShapeAt(playerID : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y);
function NxNSquareShapeAtDouble(playerID : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y);

var x = 0;
var y = 0;

function main(playerID)
{
   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   MoveUnit(All, "40 + 1n Gantrithor", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "50 + 1n Tank", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition");

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)      //0.00
      {
         RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] % 2 == 0 && v.P_LoopMain[playerID] < 64)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Table_Sin(playerID, 45 * (v.P_LoopMain[playerID] / 2), 64);
            trg.Table_Cos(playerID, 45 * (v.P_LoopMain[playerID] / 2), 64);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Double(playerID, 1, "60 + 1n Danimoth", x, y);
            trg.Shape_Double(playerID, 1, "Protoss Dark Archon", x, y);
            trg.Shape_Dot(playerID, 1, "40 + 1n Mojo", 0, 0);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, "Anywhere");
         }

         if (v.P_LoopMain[playerID] >= 8 && v.P_LoopMain[playerID] < 14)    //0.64 - 1.12
         {
            var i = v.P_LoopMain[playerID] - 8;

            if (i < 4)
            {
               trg.Table_Sin(playerID, 0, 50 + 50 * i);
               trg.Table_Cos(playerID, 0, 50 + 50 * i);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "40 + 1n Mojo", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);

               KillUnitAt(All,  "60 + 1n Archon", "Anywhere", playerID);

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            }

            if (i == 4)
            {
               trg.Table_Sin(playerID, 0, 200);
               trg.Table_Cos(playerID, 0, 200);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Siege", x, y);

               KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            }
         }
         if (v.P_LoopMain[playerID] >= 14 && v.P_LoopMain[playerID] < 20)   //1.12 - 1.60
         {
            var i = v.P_LoopMain[playerID] - 14;

            if (i < 4)
            {
               trg.Table_Sin(playerID, 45, 50 + 50 * i);
               trg.Table_Cos(playerID, 45, 50 + 50 * i);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "40 + 1n Mojo", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);

               KillUnitAt(All,  "60 + 1n Archon", "Anywhere", playerID);

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            }

            if (i == 4)
            {
               trg.Table_Sin(playerID, 45, 200);
               trg.Table_Cos(playerID, 45, 200);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Siege", x, y);

               KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            }
         }

         if (v.P_LoopMain[playerID] >= 30 && v.P_LoopMain[playerID] < 64)    //1.92
         {
            var i = v.P_LoopMain[playerID] - 30;

            if (i == 0) 
            {
               trg.Table_Sin(playerID, 22, 100);
               trg.Table_Cos(playerID, 22, 100);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }
            if (i == 6) 
            {
               trg.Table_Sin(playerID, 67, 150);
               trg.Table_Cos(playerID, 67, 150);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }            
            if (i == 12) 
            {
               trg.Table_Sin(playerID, 67, 100);
               trg.Table_Cos(playerID, 67, 100);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }            
            if (i == 18) 
            {
               trg.Table_Sin(playerID, 22, 150);
               trg.Table_Cos(playerID, 22, 150);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }
            if (i == 24) 
            {
               trg.Table_Sin(playerID, 22, 100);
               trg.Table_Cos(playerID, 22, 100);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }
            if (i == 30) 
            {
               trg.Table_Sin(playerID, 67, 150);
               trg.Table_Cos(playerID, 67, 150);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];
            }

            if (i % 6 == 0)
            {
               KillUnitAt(All, "Protoss Reaver", "Anywhere", playerID);

               trg.Shape_Square(playerID, 1, "Protoss Reaver", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", x, y);

               KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

               ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               MoveUnit(All, "Protoss Reaver", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            }
         }
         if (v.P_LoopMain[playerID] == 64)      //5.12
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", playerID);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            s.CharacterVoice(17);            
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 72)      
         {
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 1)    //5.80
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            NxNSquareShapeAt(playerID, 1, "60 + 1n Danimoth", 2, 75, 100, 0);
            NxNSquareShapeAt(playerID, 1, "60 + 1n High Templar", 2, 75, 100, 0);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }

         if (v.P_LoopMain[playerID] == 4)    //6.12
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            NxNSquareShapeAt(playerID, 1, "60 + 1n Danimoth", 2, 75, 100, 100);
            NxNSquareShapeAt(playerID, 1, "60 + 1n High Templar", 2, 75, 100, 100);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }

         if (v.P_LoopMain[playerID] == 8)    //6.44
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 12)
         {
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 2)    //6.80
      {
         if (v.P_LoopMain[playerID] < 4)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 50 - 50 * v.P_LoopMain[playerID], 100);
            trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 50 - 50 * v.P_LoopMain[playerID], 100);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         if (v.P_LoopMain[playerID] == 4)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 5, 75);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n High Templar", 5, 75);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         if (v.P_LoopMain[playerID] == 8)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 3, 75);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n High Templar", 3, 75);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         if (v.P_LoopMain[playerID] == 12)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 16)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
            s.CharacterVoice(18);            

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 3) //8.10
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            for (var k = 0; k < 8; k++)
            {
               CreateUnit(4, "60 + 1n Siege", k + 33, playerID);
               SetInvincibility(Enable, "60 + 1n Siege", playerID, "[Skill]Unit_Wait_ALL");
            }
         }

         var i = v.P_LoopMain[playerID] % 4;

         if (v.P_LoopMain[playerID] % 8 == 0)
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", playerID);
         }

         var r = ((v.P_LoopMain[playerID] / 4) % 2) * 45 + 22;

         if (i % 2 == 0) 
         {
            trg.Table_Sin(playerID, r, 50 + 50 * i);
            trg.Table_Cos(playerID, r, 50 + 50 * i);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];
            
           trg.Shape_Square(playerID, 1, "Protoss Reaver", x, y);
         }
         if (i % 2 == 1) 
         {
            trg.Table_Sin(playerID, r + 22, 50 + 50 * i);
            trg.Table_Cos(playerID, r + 22, 50 + 50 * i);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];
         }

         if (i % 4 == 3)
         {
           trg.Shape_Square(playerID, 1, "40 + 1n Lurker", x, y);
         }

         RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

         trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", x, y);
         trg.Shape_Square(playerID, 1, "Protoss Dark Archon", x, y);

         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);

         ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         MoveUnit(All, "Protoss Reaver", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
         MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
         Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         
         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 20)
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", playerID);
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
            KillUnitAt(All, "40 + 1n Lurker", "Anywhere", playerID);
            
            s.CharacterVoice(19);            

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 4) //9.90
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            epic.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 3, 75, 1);

            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere");
         }
         if (v.P_LoopMain[playerID] == 4)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 3, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] == 6)
         {
            trg.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 3, 75);

            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere");
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 10)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 3, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);

            s.CharacterVoice(20);            

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 5) //10.70
      {
         if (v.P_LoopMain[playerID] < 8)
         {
            if (v.P_LoopMain[playerID] % 2 == 0)
            {
               trg.Table_Sin(playerID, v.P_LoopMain[playerID] * 45, 150);
               trg.Table_Cos(playerID, v.P_LoopMain[playerID] * 45, 150);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               NxNSquareShapeAtDouble(playerID, 1, "40 + 1n Gantrithor", 3, 50, x, y);
               NxNSquareShapeAtDouble(playerID, 1, "50 + 1n Tank", 2, 75, x, y);

               for (var i = 0; i < 8; i++)
               {
                  trg.MoveLoc("50 + 1n Tank", playerID, 0, 0);
                  RemoveUnitAt(1, "50 + 1n Tank", "Anywhere", playerID);
                  MoveUnit(1, "60 + 1n Siege", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
               }
            }

            if (v.P_LoopMain[playerID] % 2 == 1)
            {
               trg.Table_Sin(playerID, v.P_LoopMain[playerID] * 45, 150);
               trg.Table_Cos(playerID, v.P_LoopMain[playerID] * 45, 150);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               NxNSquareShapeAtDouble(playerID, 1, "50 + 1n Battlecruiser", 3, 50, x, y);
               NxNSquareShapeAtDouble(playerID, 1, "Protoss Reaver", 2, 75, x, y);

               KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
               KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

               ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               MoveUnit(All, "Protoss Reaver", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            }
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 18)
         {
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;         
         }
      }
      else if (v.P_CountMain[playerID] == 6)    //9.90
      {
         KillUnitAt(All, "Protoss Reaver", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}

function NxNSquareShapeAt(playerID : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y)
{
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, x, y);
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, -x, -y);
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, -y, x);
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, y, -x);
}

function NxNSquareShapeAtDouble(playerID : TrgPlayer, count, Unit : TrgUnit, n, interval, x, y)
{
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, x, y);
   adv.Shape_NxNSquareAt2(playerID, count, Unit, n, interval, -x, -y);
}


